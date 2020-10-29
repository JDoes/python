type = input("Are you hybrid, or remote? ")

if (type.lower() == "hybrid"):
    day = input("\nWhich days are you in person?"+
                "\n(Mon Wed or Tues Thurs)")
    
    if (day.lower() == "mon wed" or day.lower() == "monday wednesday"):
        print("\nFollow the direct instruction Mon and Wed, "+
              "\nand work independently on Edhesive Tues and Thurs.")
    
    elif (day.lower() == "tues thurs" or day.lower() == "tuesday thursday"):
        print("\nFollow the direct instruction Tues and Thurs, "+
              "\nand work independently on Edhesive Mon and Wed.")
    
    else:
        print("Invalid day. Must enter "+
              "\n\"mon wed (or monday wednesday)\", "+
              "\nor \"tues thurs (or tuesday thursday)\"")
        
elif (type.lower() == "remote"):
    print("\nRemote scholars are already "+
          "\nused to what to do: "+
          "\nreceive direct instruction on Mon Wed, "+
          "\nand work independently "+
          "\nin Edhesive on Tues and Thurs.")

else:
    print("Invalid option. "+
          "\nMust choose \"hybrid\" or \"remote\"")
