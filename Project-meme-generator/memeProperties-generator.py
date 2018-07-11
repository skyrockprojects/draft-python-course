from memeProperties import Meme

thanos = Meme("https://skrck.pro/thanos", "thanos", "epic funny", "fortnite dance")
thanos.save()
thanos.show()
thanos.top = "i am"
thanos.bottom = "big mans"
thanos.getImage() # you have to reset the image to get rid of the captions
thanos.addCaption()
thanos.save()
thanos.show()