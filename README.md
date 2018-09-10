# GoogleHome meets RaspberryMatic via IFTTT

I have a Google Home, and also some blinds and window openers by HomeMatic and WinMatic, using [Jens Maus' RaspberryMatic](https://github.com/jens-maus/RaspberryMatic). I to simply tell my Google Home to close my window (and other stuff) without having to get out of bed. So this project will connect your Google Home with your RaspberryMatic, via [Webhooks of IFTTT](https://ifttt.com/maker_webhooks).

You can give an oral commando to your Google Home using the [Google Assistant Trigger Manager in IFTTT](https://ifttt.com/create/if-google_assistant?sid=1) ("this"). Then you need the [Webhook Action in IFTTT](https://ifttt.com/create/if-say-a-simple-phrase-then-maker_webhooks?sid=5) ("that") to call a service, which is programmed in Python (but I am sure that this can be rewritten easily in any language you like) running on a server in your home (could be your Raspberry Pi, or any other machine, just make sure that your router forwards forward requests coming in from IFTTT). The Python program will then forward the command your RaspberryMatic using selenium (opening up the Webpage of RaspberryMatic, and clicking the right command).

I only spent about 2h on this, and it works just nicely. But it's certainly far from perfect. I would be excited if somebody wants to join this project and improve the code. 

Some ideas for improvement:
- Secure the Python web service a bit better.
- Program/use an API on RaspberryMatic (without the clumsy selenium solution).
- Generally a better integration with RaspberryMatic, maybe even a nice extension.
