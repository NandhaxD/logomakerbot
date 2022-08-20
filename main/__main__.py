from main import pyrobot, support 

if __name__ == "__main__":
   pyrobot.run()
   with pyrobot:
      await pyrobot.send_message(f"@{support}",message="yeah")
