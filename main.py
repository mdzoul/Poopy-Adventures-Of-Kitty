print('''

 
               /\____/\    __
             .'  """"  `,-'  `--.__
        __,- :   -  -  ;  " ::     `-. -.__
     ,-sssss `._  `' _,'"     ,'~~~::`.sssss-.
    |ssssss ,' ,_`--'_    __,' ::  `  `.ssssss|
   |sssssss `-._____~ `,,'_______,---_;; ssssss|
    |ssssssssss     `--'~{__   ____   ,'ssssss|
     `-ssssssssssssssssss ~~~~~~~~~~~~ ssss.-'
          `---.sssssssssssssssssssss.---' Susie Oviatt


''')

print("Good morning, Kitty. You have just woken up from your owner's bed. It was a good long nap. You feel a little disoriented but now there is a sense of urgency rising within you.\n")
print("Your mission is to poop.\n") 

# Door/Stay
door_stay = input("You look around you and you see the door.\n\nDo you choose to go to the [door] or [stay]?\n")

if door_stay == "door":
  print("\nYou manage to fumble towards the door and see a fork in the hallway.")
  
  # Masterbedroom/Living room/Guest room - Start
  print("\nYou know this house like the back of your paw.\n\nThe living room is [straight] ahead.\nThe masterbedroom is on your [left].\nThe guest bedroom is on your [right].")  
  mlg_room = input("\nNow, the location of your litter box would be in this direction:\n")
  
  if mlg_room == "straight":
    print("\nYou continue walking into the living room and are greeted by familiar sights and smells.")

    # Walk straight/Go to food bowl - Start
    print("\nYou see one of your humans lying on the floor playing with her phone.\nYou also smell the irresistable scent of your favourite dry food in your food bowl right beside you.")
    walk_eat = input("\nDo you continue [walk]ing, or do you fall for the aroma in the [food] bowl?\n")
    
    if walk_eat == "walk":
      print("\nYou walk towards your human but she has not noticed you yet.")
      towards_around = input("\nDo you want to continue walking [past] your human,\nOr do you want to walk [around] her?\n")

      # Approach human/Walk around human - Start
      if towards_around == "around":
        print("\nYour human was too engrossed in her phone that she does not notice you walking around her.\nYou get to the litter box in the living room, but there was a problem.\n\nYour brother is using the litter box.\nAnd he does not seem to be done anytime soon.")
        print("\nYou start to panic but that just makes the situation worse.\nI dare say, the more you panic, the shittier the situation becomes.")

        # Second litter box/Guest toilet - Start
        print("\nYou remember there is a second litter box in the kitchen.\nYou sprint as fast as you can, barely holding on anymore.\nYou are trying to keep it together as you tell yourself that the litter box is at the end of the kitchen after the guest toilet.\nYou don't know if you are going to make it.")
        box_toilet = input("\nAs you are about to run past the [guest toilet] towards the [litter box] at the end of the kitchen, you made the daring decision to use the:\n")

        if box_toilet == "guest toilet":
          print("\nYou saw that the guest toilet doors were closed.\nYou had to think fast if you want to [meow] as loud as you can to let yourself in or [push] the doors with all your might.")

          # Push door/Meow loudly - Start
          push_meow = input("\nIn a fit of hysteria, you decided to:\n")

          if push_meow == "push":
            print("\nYou stood up on your hind legs and pushed the doors open with your body weight in one go.\n\nThe toilet was empty!\n\nYou climbed onto the edge of the toilet seat and finally flushed all that stress and tension away.")
            print("\nNicely Done, Kitty! Good job!")

          else:
            print("\nYou made a mistake.\n\nThe moment you squeezed that tiny diaphragm to let out the loudest meow you can possibly muster, you also contracted your abdominal muscles a little too hard.")
            print("\nYour fierce meow becomes a meow of embarrassment as you ask your humans to help you clean your mess.\nSuch a disappointment.")
            print("\nGame Over.")
              
          # Push door/Meow loudly - Start

        
        else:
          print("\nYou got to the end of the kitchen!\nYou managed to hold it in as you enter the litter box.")
          print("\nOnly to find that there was no litter in the litter box.\nIt was too late to turn back to use the guest toilet.\nYou let yourself and your dignity go.")
          print("\nGame Over.")

        # Second litter box/Guest toilet - End

      else:
        print("\nYou try to stealthily walk past your human, in hopes that she is too engrossed in her phone to not notice you.\nUnfortunately, in the moment that you do, she looked away from her phone and saw you.\nShe picks you up and starts cuddling and hugging you.")
        print("\nIt does not end well for both you and your human.")
        print("\nGame Over.")

      # Approach human/Walk around human - End

    
    else:
      print("\nYou indulge in the crunchy and sweet taste of your food.\nYou forget about the world and your problems as you take another bite, and then another.")
      print("\nSuddenly, you feel something gurgling in your gut.\nHow could you have forgotten your goal?\nDarn these tasty treats.\nNow you're too heavy to rush to the toilet.")
      print("\nYou cannot hold back as you shate where you ate.")
      print("\nGame Over.") #Would love to learn how to loop this. Check flowchart

    # Walk straight/Go to food bowl - End
    
  elif mlg_room == "left":
    print("\nYou rush to the masterbedroom toilet.\nYou pushed on the toilet door in anticipated relief only to find out that one of your humans is occupying it\nToo late.\nYour anticipated relief just became an accidental one.")
    print("\nGame Over.")
  elif mlg_room == "right":
    print("\nYou decided to take a detour and enter the guest bedroom for some reason.\nAs you enter the bedroom, you trip on the door stopper.\nYou wander about in the guest bedroom not realising that the door is slowly closing behind you.")
    print("\nSLAM! The door shut close.")
    print("\nGame Over.")

  # Masterbedroom/Living room/Guest room - End

else:
  print("\nYou decide to close your eyes and nap a bit more.\nYou wake up to a pile of your own poop on your owner's bed.\nYour owner screams at you.\nLooks like you're sleeping outside tonight.")
  print("\nGame Over.")
