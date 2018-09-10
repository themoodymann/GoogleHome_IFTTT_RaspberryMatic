# GoogleHome meets RaspberryMatic via IFTTT

I have a Google Home, and also some blinds and window openers by HomeMatic and WinMatic, using [Jens Maus' RaspberryMatic](https://github.com/jens-maus/RaspberryMatic). I want to simply tell my Google Home to, e.g., close my Winmatic powered bedroom window without having to get out of bed. So this project will connect your Google Home with your RaspberryMatic, via [IFTTT](https://ifttt.com).

You can give an oral command ("Close Window") to your Google Home using the [Google Assistant Trigger Manager in IFTTT](https://ifttt.com/create/if-google_assistant?sid=1) (this is the "this" part of IFTTT). Then you need the [Webhook Action in IFTTT](https://ifttt.com/create/if-say-a-simple-phrase-then-maker_webhooks?sid=5) (the "that" part of IFTTT) to call a service. There added an example of such an IFTTT recipe. IFTTT then calls the service programmed in Python running on a server in your home (on your Raspberry Pi, or any other machine; just make sure that you told your router to forward that port). The Python program will then forward the command to your RaspberryMatic using selenium (opening up the web interface of RaspberryMatic, "clicking" the correct XPath).

I only spent about 2h on this, and it works nicely. But it's certainly far from perfect. I would be excited if somebody wants to join this project and improve the code. 

Some ideas for improvement:
- Secure the Python web service a bit better by adding a password.
- Give Python program a simple user interface.
- Automate the IFTTT part so that the IFTTT bridge does not have to be added manually.
- Skip IFTTT completely by programming the Webhook directly in Google Home.
- Program/use an API on RaspberryMatic (without the clumsy selenium solution).
- Generally a better integration with RaspberryMatic, maybe as an extension.
