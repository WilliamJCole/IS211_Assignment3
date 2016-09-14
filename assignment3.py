#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211_Assignment3"""

import urllib2
import re
import argparse

def main():
    '''Main Func'''

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Enter the URL to get the CSV file.')
    args = parser.parse_args()

    if args.url:
        try:
            content = downloadData(args.url)
            imageSearch(content)
        except:
            print 'The URL entered is invalid.'
    else:
        print 'Please enter a URL.'


def downloadData(url):
    """Func to import data file."""
    response = urllib2.urlopen(url) #opens file
    html = response.read() #reads file data
    return html #returns file data


def imageSearch(url):
    """Func to import image % in file."""

    total = 0
    images = 0

    for row in url:
        total += 1
        img_ext = ('([.jpg$]|[.png$]|[.jpeg$]|[.gif$]|[.JPG$]|[.PNG$]|[.JPEG$]|[.GIF$])')
        #characters to search in file
        if re.search(img_ext, row) is not None:
            images += 1

    image_pct = (float(images) / total) * 100 #formula to calculate image % in file
    pct = 'Image requests account for {0:0.1f}% of all requests'.format(image_pct)
    return pct


def browserSearch(url):
    """Func to import most popular browser being used."""
    total = 0
    sites = 0

    for line in url:
        browsers = ('([Chrome]|[Firefox]|[Safari]|[MSIE])')
        if re.search(browsers, line) is not None:
            sites +=1
    hits = (total + sites)
    total_hits = 'The most popular browser is {0:0.1f}% of all requests'.format(hits)
    return total_hits

def countHits(mydata):
    '''This func counts the number of hits/hr.

    Args:
        mydata (dictionary): A dict containing the log file.

    '''
    hourlist = []
    for key, value in mydata.iteritems():
        timestamp = datetime.datetime.strptime(value[0], '%Y-%m-%d %H:%M:%S')
        hour = datetime.datetime.strftime(timestamp, '%H')
        hourlist.append(hour)
    hourdict = Counter(hourlist)
    for h in sorted(hourdict, key=hourdict.get, reverse=True):
        print ("Hour {} has {} hits.").format(h, hourdict[h])



if __name__ == "__main__":
    #url = ' http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

    main()
