print('''\33[90m


               /\____/\    __
             .'  """"  `,-'  `--.__
        __,- :   -  -  ;  " ::     `-. -.__
     ,-sssss `._  `' _,'"     ,'~~~::`.sssss-.
    |ssssss ,' ,_`--'_    __,' ::  `  `.ssssss|
   |sssssss `-._____~ `,,'_______,---_;; ssssss|
    |ssssssssss     `--'~{__   ____   ,'ssssss|
     `-ssssssssssssssssss ~~~~~~~~~~~~ ssss.-'
          `---.sssssssssssssssssssss.---'


\33[0m''')

print("Good morning, Kitty. You have just woken up from your owner's bed. It was a good long nap. You feel a little disoriented but now there is a sense of urgency rising within you.\n")
print("\33[1;4mYour mission is to poop.\33[0m\n")

# Door/Stay
door_stay = input("You look around you and you see the door.\n\nDo you choose to go to the \33[32m[door]\33[0m or \33[32m[stay]\33[0m?\n").lower()

if door_stay == "door":
  print("---\nYou manage to fumble towards the door and see a fork in the hallway.")

  # Masterbedroom/Living room/Guest room - Start
  print("\nYou know this house like the back of your paw.\n\nThe living room is \33[32m[straight]\33[0m ahead.\nThe masterbedroom is on your \33[32m[left]\33[0m.\nThe guest bedroom is on your \33[32m[right]\33[0m.")
  mlg_room = input("\nNow, the location of your litter box should be in this direction:\n").lower()

  if mlg_room == "straight":
    print("---\nYou continue walking into the living room and are greeted by familiar sights and smells.")

    # Walk straight/Go to food bowl - Start
    print("\nYou see one of your humans lying on the floor playing with her phone.\nYou also smell the irresistable scent of your favourite dry food in your food bowl right beside you.")
    walk_eat = input("\nDo you continue \33[32m[walk]\33[0ming, or do you fall for the aroma in the \33[32m[food]\33[0m bowl?\n").lower()

    if walk_eat == "walk":
      print("---\nYou walk towards your human but she has not noticed you yet.")
      towards_around = input("\nDo you want to continue walking \33[32m[past]\33[0m your human,\nOr do you want to walk \33[32m[around]\33[0m her?\n").lower()

      # Approach human/Walk around human - Start
      if towards_around == "around":
        print("---\nYour human is too engrossed in her phone that she does not notice you walking around her.\nYou get to the litter box in the living room, but there is a problem.\n\nYour brother is using the litter box.\nAnd he does not seem to be done anytime soon.")
        print("\nYou start to panic but that just makes the situation worse.\nI dare say, the more you panic, the shittier the situation becomes.")

        # Second litter box/Guest toilet - Start
        print("\nYou remember there is a second litter box in the kitchen.\nYou sprint as fast as you can, barely holding on anymore.\nYou are trying to keep it together as you tell yourself that the litter box is at the end of the kitchen after the guest toilet.\nYou don't know if you are going to make it.")
        box_toilet = input("\nAs you are about to run past the \33[32m[guest toilet]\33[0m towards the \33[32m[litter box]\33[0m at the end of the kitchen, you make the daring decision to use the:\n").lower()

        if box_toilet == "guest toilet":
          print("---\nYou see that the guest toilet doors are closed.\nYou have to think fast whether you want to \33[32m[meow]\33[0m as loud as you can to let yourself in or \33[32m[push]\33[0m the doors with all your might.")

          # Push door/Meow loudly - Start
          push_meow = input("\nIn a fit of hysteria, you decide to:\n").lower()

          if push_meow == "push":
            print("---\nYou stand up on your hind legs and push the doors open with your body weight in one go.\n\nThe toilet is empty!\n\nYou climb onto the edge of the toilet seat and finally flush all that stress and tension away.")
            print("\n\33[1;32mNicely Done, Kitty! Good job!\33[0m")

          elif push_meow == "meow":
            print("---\nYou made a mistake.\n\nThe moment you squeezed that tiny diaphragm to let out the loudest meow you can possibly muster, you also contracted your abdominal muscles a little too hard.")
            print("\nYour fierce meow becomes a meow of embarrassment as you ask your humans to help you clean your mess.\nSuch a disappointment.")
            print("\n\33[31mGame Over.\33[0m")

          else:
            print("\n\33[31m[Invalid input. Please rerun.]\33[0m")
              
          # Push door/Meow loudly - End


        elif box_toilet == "litter box":
          print("---\nYou get to the end of the kitchen!\nYou manage to hold it in as you enter the litter box.")
          print("\nOnly to find that there is no litter in the litter box.\nIt is too late to turn back to use the guest toilet.\nYou let yourself and your dignity go.")
          print("\n\33[31mGame Over.\33[0m")

        else:
          print("\n\33[31m[Invalid input. Please rerun.]\33[0m")
        # Second litter box/Guest toilet - End

      elif towards_around == "past":
        print("---\nYou try to stealthily walk past your human, in hopes that she is too engrossed in her phone to not notice you.\nUnfortunately, in the moment that you do, she looked away from her phone and saw you.\nShe picks you up and starts cuddling and hugging you.")
        print("\nIt does not end well for both you and your human.")
        print("\n\33[31mGame Over.\33[0m")

      else:
        print("\n\33[31m[Invalid input. Please rerun.]\33[0m")
      # Approach human/Walk around human - End


    elif walk_eat == "food":
      print("---\nYou indulge in the crunchy and sweet taste of your food.\nYou forget about the world and your problems as you take another bite, and then another.")
      print("\nSuddenly, you feel something gurgling in your gut.\nHow could you have forgotten your goal?\nDarn these tasty treats.\nNow you're too heavy to rush to the toilet.")
      print("\nYou cannot hold back as you shate where you ate.")
      print("\n\33[31mGame Over.\33[0m") #Would love to learn how to loop this. Check flowchart

    else:
      print("\n\33[31m[Invalid input. Please rerun.]\33[0m")
    # Walk straight/Go to food bowl - End

  elif mlg_room == "left":
    print("---\nYou rush to the masterbedroom toilet.\nYou push on the toilet door in anticipated relief only to find out that one of your humans is occupying it\nToo late.\nYour anticipated relief just became an accidental one.")
    print("\n\33[31mGame Over.\33[0m")
  elif mlg_room == "right":
    print("---\nYou decide to take a detour and enter the guest bedroom for some reason.\nAs you enter the bedroom, you trip on the door stopper.\nYou wander about in the guest bedroom not realising that the door is slowly closing behind you.")
    print("\nSLAM! The door shut close.")
    print("\n\33[31mGame Over.\33[0m")

  else:
    print("\n\33[31m[Invalid input. Please rerun.]\33[0m")
    
  # Masterbedroom/Living room/Guest room - End

elif door_stay == "stay":
  print("---\nYou decide to close your eyes and nap a bit more.\nYou wake up to a pile of your own poop on your owner's bed.\nYour owner screams at you.\nLooks like you're sleeping outside tonight.")
  print("\n\33[31mGame Over.\33[0m")

else:
  print("\n\33[31m[Invalid input. Please rerun.]\33[0m")