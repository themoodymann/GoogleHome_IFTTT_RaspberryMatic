# GoogleHome meets RaspberryMatic via IFTTT

I have a Google Home, and also some blinds and window openers by HomeMatic and WinMatic, using [Jens Maus' RaspberryMatic](https://github.com/jens-maus/RaspberryMatic). For example, I want to simply tell my Google Home to close my bedroom window without having to get out of bed. So this project will connect your Google Home with your RaspberryMatic, via [IFTTT](https://ifttt.com).

You orally tell your Google Home what to do ("Close Window"), using the [Google Assistant Trigger Manager in IFTTT](https://ifttt.com/create/if-google_assistant?sid=1) (this is the "this" part of IFTTT). Then you need the [Webhook Action in IFTTT](https://ifttt.com/create/if-say-a-simple-phrase-then-maker_webhooks?sid=5) (the "that" part of IFTTT) to call a service. In this repository there is an example of such an IFTTT recipe. IFTTT then calls the service programmed in Python running on a server in your home (on your Raspberry Pi, or any other machine; just make sure that you told your router to forward that port to the correct local IP address). The Python program will then forward the command to your RaspberryMatic using selenium (opening up the web interface of RaspberryMatic, "clicking" the correct XPath).

I only spent about 2h on this, and it works nicely. But it's certainly far from perfect. If somebody wants to join this project and improve the code, here some ideas for improvement:
- Secure the Python web service a bit better by adding a password.
- Give Python program a simple user interface.
- Automate the IFTTT part so that the IFTTT bridge does not have to be added manually.
- Skip IFTTT completely by programming the Webhook directly in Google Home.
- Program/use an API on RaspberryMatic (without the clumsy selenium solution).
- Generally a better integration with RaspberryMatic, maybe as an extension.
