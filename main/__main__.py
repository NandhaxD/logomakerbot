from main import pyrobot, support 

if __name__ == "__main__":
   pyrobot.run()
   with pyrobot:
      pyrobot.send_message(f"@{support}",message="yeah")
