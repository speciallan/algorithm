
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """

        shortUrl = ''
        
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """

        longUrl = ''

        return longUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == "__main__":
    
    longUrl = 'http://speciallan.com/problem535.html'
    # http://tinyurl.com/3k2i1d

    c = Codec()
    shortUrl = c.encode(longUrl)
    longUrl2 = c.decode(shortUrl)

    print(longUrl)
    print(shortUrl)
    print(longUrl)
