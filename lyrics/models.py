from django.db import models
    
class Artist(models.Model):
    kanji = models.TextField('kanji name')
    romaji = models.TextField('romaji name')
    english = models.TextField('english name')
    def __str__(self):
        return self.romaji
    
class Staff(models.Model):
    kanji = models.TextField('kanji name')
    romaji = models.TextField('romaji name')
    english = models.TextField('english name')
    def __str__(self):
        return self.romaji

class Lyric(models.Model):
    title_kanji = models.TextField('song title in kanji')
    title_romaji = models.TextField('song title in romaji')
    title_english = models.TextField('song title in english')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    lyricist = models.ForeignKey(Staff, on_delete=models.CASCADE)
    composer = models.ForeignKey(Staff, on_delete=models.CASCADE)
    arranger = models.ForeignKey(Staff, on_delete=models.CASCADE)
    release_date = models.DateTimeField('date of song release')
    pub_date = models.DateTimeField('date published')
    
    kanji = models.TextField('kanji lyrics')
    romaji = models.TextField('romaji lyrics')
    english = models.TextField('english lyrics')

    def __str__(self):
        return self.title_romaji