import requests
import webbrowser

print(f'Daily Treasure Claim Nodepay Multiple Account') 

def dailyclaim():
    try:
        with open('token_list.txt', 'r') as file:
            local_data = file.read().splitlines()
            for tokenlist in local_data:
                url = f"http://api.nodepay.ai/api/mission/complete-mission?"
                headers = {
                    "Authorization": f"Bearer {tokenlist}",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                    "Content-Type": "application/json",
                    "Origin": "https://app.nodepay.ai",
                    "Referer": "https://app.nodepay.ai/"
                }
                
                data = {
                    "mission_id": "1"
                }

                response = requests.post(url, headers=headers, json=data)
                is_success = response.json().get('success')
                
                if is_success == True:
                    print(f'Claim Reward Success!')
                    print(response.json())
                    webbrowser.open("https://www.youtube.com/watch?v=V45XaQm6bGg&t=231s")
                else:
                    print(f'Reward Already Claimed! Or Something Wrong!')
                    print(response.json())
                    webbrowser.open("https://www.youtube.com/watch?v=V45XaQm6bGg&t=231s")
    except Exception as e:
        print(f"Error : {e}")
    
dailyclaim()

# Credit:
print("\n==============================")
print("Developed by: Dasar Pemulung")
print("Join Telegram Channel: @dasarpemulung")
print("YouTube: Dasar Pemulung")
print("==============================")
