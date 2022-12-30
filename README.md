<h1 align="center">
	<img src="https://i.postimg.cc/Hc7NSz24/ukiyo.jpg" width="200px"><br>
    Ukiyo - a simple, minimalist and efficient discord vanity URL sniper.
</h1>

<p align="center">
	Ukiyo is easy to use, has a very visually pleasing interface, and has great speed.
</p>

<p align="center">
	<a href="https://deno.land" target="_blank">
    	<img src="https://img.shields.io/badge/Version-1.3.1-7DCDE3?style=for-the-badge" alt="Version">
</p>
	
# NOTE
- Please read all of this, as it will save both you and me a lot of time. I don't want people opening useless issues asking for help with something covered here.
- Though this tool is 100% safe to use, i understand that people are paranoid about getting disabled. So, i would recommend using this on an alternate account with permissions to change the vanity URL, rather than using it on your main account.
- This project is NOT maintained.

# Features
- Cross-platform (Works On Windows AND Linux.)
- Single vanity and multi vanity sniping
- Very colourful interface
- User friendly
- Proxy support
- Very fast
	
# Setup
	
You can setup ukiyo by simply opening your terminal/console and pasting in the following command:
```
python setup.py
```
Or you can install the required modules manually by pasting in the following command:

```
pip install -r requirements.txt
```
After that, you want to open the config file(config.json) and input the following values:
- Your discord token. (this has to be your user token, not a bot token.)
- A webhook to send the information to.

If you want to configure multi vanity sniping, open vanities.txt and input the vanity URLs you want to snipe.

<h1 align="left">
	<img src="https://cdn.discordapp.com/attachments/925859840734167122/926380233999913000/config.png" width="250px"><br>
</h1>

### If you don't know how to do either, here are tutorials on both:

- [How to get your discord token ](https://www.youtube.com/watch?v=3qzpmTIQ-Gs)
- [How to create a discord webhook](https://www.youtube.com/watch?v=fKksxz2Gdnc)

After you've done all that, you can finally run ukiyo by typing in the following command:
```
python main.py
```

# FAQ
- **Q : Now that the installation is done, how do you actually use the tool?** 
- *A : Run it, input the required data and watch the magic happen!*

- **Q: Why doesn't it work?**
- *A : The only situations in which i can imagine the tool doesn't work are the following : you're using a bot token instead of a user token, you have no internet connection, your config is messed up(either the webhook or the user token are invalid, maybe both).*

- **Q : What should i do if i have an error that isn't listed above?**
- *A : Open an issue, describe your problem, include the error message you're getting(you can leave this out if its a bug and not a program error), provide screenshots whenever possible and i'll get back to you as soon as i can.*

- **Q : Why am i getting ratelimited after sniping a vanity URL?**
- *A : Due to the multi-threading, multiple threads are sending a request to the same URL. So, you're getting ratelimited because you're sending an abnormal amount of requests to the same URL. Don't worry though, you'll still have the vanity you sniped :D*

- **Q : How to i disable @everyone pings when i snipe a vanity URL?**
- *A : Well, i would add a yes/no ping option. But i'm way too lazy, so you can disable this by opening any text editor and replacing every line that has ||@everyone|| with a blank space. You can do this using the "replace" feature. Which i assume EVERY text editor has.*

# To do
- [x] Add multi-vanity sniping (credits to [hoemotion](https://github.com/hoemotion) for suggesting this feature)
- [ ] Add vanity swapping capabilities (switch vanities from one discord server to another)
- [x] Add multi-threading for maximum speed
- [x] Add proxy support 

# Screenshots/Videos
### [Watch The Ukiyo Showcase Here](https://youtu.be/75eJgAr16mY)
![image](https://cdn.discordapp.com/attachments/925454981203656704/927486480312573972/1x.png)
![image](https://cdn.discordapp.com/attachments/925454981203656704/927486480052539392/2x.png)
![image](https://cdn.discordapp.com/attachments/925454981203656704/927486479733784616/3x.png)

# Credits
```
github.com/1x12
```

### Contribution;
###### All contributions are accepted, just open an issue / pull request and i will get back to you as soon as i can.
