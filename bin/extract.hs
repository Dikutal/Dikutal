#!/usr/bin/env runghc
{-# LANGUAGE OverloadedStrings, TupleSections #-}
module Main(main) where

-- The input to this program should be a directory of article dumps
-- from old Dikutal, which must already be converted to UTF-8 and
-- without encoding errors in their file names.

import System.Time.Parse
import System.Locale
import Control.Applicative
import Control.Arrow
import Control.Monad
import Control.Monad.State
import qualified Data.Map as M
import Data.Maybe
import Data.Monoid
import qualified Data.Text as T
import qualified Data.Text.IO as T
import System.Directory
import System.Environment
import System.FilePath
import Text.HTML.TagSoup
import System.Time

type Page = [Tag T.Text]

data Article = Article { articleContent :: [Tag T.Text]
                       , articleAuthor :: T.Text
                       , articleDate :: CalendarTime
                       , articleTopics :: [T.Text]
                       , articleTitle :: T.Text
                       }

parseFile :: FilePath -> IO Page
parseFile = liftM (canonicalizeTags . parseTags) . T.readFile

article :: Page -> Article
article p = Article { articleContent = content p
                    , articleAuthor = author p
                    , articleDate = date p
                    , articleTopics = topics p
                    , articleTitle = title p
                    }

renderToFiles :: FilePath -> Article -> IO ()
renderToFiles dir a = do
  T.writeFile (dir </> "content") $ tagtext $ articleContent a
  T.writeFile (dir </> "date") $ d (articleDate a) <> " 13:37"
  T.writeFile (dir </> "tags") $ T.unlines $ articleTopics a
  T.writeFile (dir </> "author") $ articleAuthor a
  T.writeFile (dir </> "teaser") $ tagtext $ teaser $ articleContent a
  T.writeFile (dir </> "title") $ articleTitle a
    where d = T.pack . formatCalendarTime defaultTimeLocale (iso8601DateFormat Nothing)
          tagtext = T.strip . renderTags

author :: Page -> T.Text
author = T.takeWhile (/=',') . T.concat . drop 2 .
         T.words . innerText . authorBlock

date :: Page -> CalendarTime
date = parseTime . T.drop 2 . T.dropWhile (/=',') . innerText . authorBlock

parseTime :: T.Text -> CalendarTime
parseTime = fromMaybe (error "Invalid time") .
            parseCalendarTime tl "%e. %B %Y - %R" . T.unpack
  where tl = defaultTimeLocale { months = [("januar","jan"),("februar","Feb")
                                          ,("marts","mar"),("april","apr")
                                          ,("maj","maj"),("juni","jun")
                                          ,("juli","jul"),("august","aug")
                                          ,("september","sep"),("oktober","okt")
                                          ,("november","nov"),("december","dec")]
                               }

topics :: Page -> [T.Text]
topics = T.lines . innerText . takeWhile (not . termsE)
         . drop 1 . dropWhile (not . termsS)
  where termsS = (==TagOpen "div" [("class", "terms")])
        termsE = (==TagClose "div")

title :: Page -> T.Text
title = innerText . takeWhile (not . titleE) . drop 1 . dropWhile (not . titleS)
  where titleS = (==TagOpen "h2" [("id", "page-header")])
        titleE = (==TagClose "h2")

authorBlock :: Page -> Page
authorBlock = takeWhile (not . authorE) . drop 1 . dropWhile (not . authorS)
  where authorS = (==TagOpen "span" [("class", "submitted")])
        authorE = (==TagClose "span")

content :: Page -> Page
content = takeWhile (not . contentE) . drop 1 . dropWhile (not . contentS)
  where contentE = (==TagClose "div")
        contentS = (==TagOpen "div" [("class", "content clear-block")])

teaser :: Page -> Page
teaser = takeWhile (not . teaserE) . drop 1 . dropWhile (not . teaserS)
  where teaserS = (==TagOpen "p" [])
        teaserE = (==TagClose "p")

extractResources :: [Article] -> ([Article], M.Map T.Text T.Text)
extractResources as = second snd $ runState (mapM extract as) (startid, M.empty)
  where startid = 0 :: Int
        extract a = do c <- mapM fixTag $ articleContent a
                       return $ a { articleContent = c }
        fixTag (TagOpen t attrs)
          | t `elem` ["a", "img"] = TagOpen t <$> mapM fixAttr attrs
        fixTag t = return t
        fixAttr ("src", src)
          | "http://dikutal.dk/" `T.isPrefixOf` src = do
          src'' <- newRes src $ return $ imagePath src
          return ("src", src'')
        fixAttr ("href", href)
          | "dikutal.dk/artikler/" `T.isInfixOf` href = do
          let href' = return $ "/artikler/" <> T.pack (takeFileName $ T.unpack href)
          ("href",) <$> newRes href href'
          | "dikutal.dk/sites/default/files/images/" `T.isInfixOf` href =
          ("href",) <$> newRes href (return $ imagePath href)
        fixAttr a = return a
        newRes k k' = maybe (new k k') return =<< gets (M.lookup k . snd)
        new k k' = do v' <- k'
                      modify $ second $ M.insert k v'
                      return v'

imagePath :: T.Text -> T.Text
imagePath = ("/media/legacy/"<>) . T.takeWhile (/='?') . T.unwords .
            take 1 . T.words . T.pack . takeFileName . T.unpack

main :: IO ()
main = do dir <- fromMaybe badargs <$> listToMaybe <$> getArgs
          createDirectoryIfMissing True "output"
          files <- dirContents dir
          interesting <- filter (not . null . articleContent . snd) <$>
                         zip files <$> map article <$>
                         mapM (parseFile . (dir </>)) files
          let (interesting', m) = first (zip $ map fst interesting) $
                                  extractResources $ map snd interesting
          forM_ interesting' $ \(file, art) -> do
            createDirectoryIfMissing True $ "output" </> file
            renderToFiles ("output" </> file) art
          forM_ (M.toList m) $ \(res, now) ->
            T.putStrLn $ "Mapping " <> res <> " to " <> now
  where badargs = error "Requires exactly one argument specifying a directory of articles."
        dirContents = liftM (filter (not . flip elem [".", ".."]))
                      . getDirectoryContents
