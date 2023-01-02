# Stemmed_Lyrics_Genre_Prediction
Using lyrics to predict the genre of a song

This project aims to apply Random Forest (RF) model to predict the genres based on the Song Lyrics. We hope those predictions can facilitate the automation of the music industry.

Genre prediction in music organization has been recognized by the industry for some time now especially after the release of music applications like Spotify, SoundCloud, and Apple Music. These applications are heavily used by the public due to the huge options of songs to choose from and nowadays, users get recommended new songs from the application’s recommendation system based on their preferences including genres. Different genres of songs have different moods which have an effect on the new recommendation’s users receive. 

Analyzing the lyrics of a song can be beneficial for the recommendation systems, hence giving the users better recommendations, enhancing the overall experience for the user. The objective of this study is to build a model that can predict a song’s genre based on the song’s lyrics. I tested several different machine learning model, Random Forest to predict the genre. There were two inputs for the models which were stemmed and lemmed lyrics. I cleaned the data by tokenizing the lyrics, removing stop words, getting a frequency of each word, then getting a tf-idf score for each word and making sure all the lyrics were in English. Ultimately, stemmed lyrics performed the best of most of the models and the Random Forest model had the best accuracy in predicting the genre of the song’s lyrics.

