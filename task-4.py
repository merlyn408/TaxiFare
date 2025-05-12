import time
def taxi_fare(x):
  base=3.00
  hund=1.00
  total=base+(hund*x)
  return total
taxi_art = r'''
        __________
       //  ||\ \ \
 _____//___||_\ \ \___
 )  _          _    \
 |_/ \________/ \___|
___\_/________\_/______
'''

print(taxi_art)
print("Welcome aboard! Let's calculate your fare with style. 🚕💨")

print("You're currently at Kochi, Kerala.")
print("Where do you want to travel?\n1:Bangalore\n2:Chennai\n3:Mumbai\n4:Kolkata\n ")
ch=int(input())

match ch:
  case 1:
    print("Ooh! Bangalore! A city that seamlessly blends tradition with modernity, offering a unique cultural experience.")
    time.sleep(2)
    print("The journey from Kochi to Bangalore spans 550 kilometers.")
    distance=550
  case 2:
    print("Ooh! Chennai! A city of the vibrant southern metropolis, where rich cultural heritage meets modern dynamism.")
    time.sleep(2)
    print("Kochi and Chennai are approximately 685 km apart.")
    distance=685
  case 3: 
    print("Ooh! Mumbai! The city of dreams, where Bollywood glamour meets bustling streets, iconic landmarks like the Gateway of India stand tall, and diverse cultures blend in a vibrant mosaic.")
    time.sleep(2)
    print("It's approximately 1586 kilometers between Kochi and Mumbai.")
    distance=1586
  case 4:
    print("Ooh! Kolkata! The City of Joy, where colonial history meets cultural richness, from iconic Howrah Bridge to vibrant Durga Puja celebrations and the intellectual legacy of Tagore's Bengali Renaissance.")
    time.sleep(2)
    print("It's a long 2230-kilometer trip from Kochi to Kolkata.")
    distance=2230
  case _:
    print("Invalid choice.")
    exit()

print("\nProcessing your booking... 🚕")
time.sleep(5)
print("Calculating your fare... 💸")
time.sleep(5)

fare = taxi_fare(distance)
print(f"\nYour total cost is: ₹{fare:.2f}")
time.sleep(3)
end_art = r'''
   _______   _______   _______   _______
  /       \ /       \ /       \ /       \
 /    ♥    \    ♥    \    ♥    \    ♥    /
/___________\_________\_________\_______/
|     THANK YOU FOR RIDING WITH US!     |
 \       Wishing you safe travels       /
  \         and smooth journeys!       /
   \__________________________________/
'''

print(end_art)
print("We hope your journey was full of joy and adventure. Until next time, travel safe! 🚕✨")
