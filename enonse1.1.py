kontinye =True
while(kontinye):
    tab = int(input("rantre yon nonb soti nan 0 pou rive nan 10: "))
    if tab> 0 and tab <= 10:
        print(f"tab {tab} miltiplikasyon")
        for i in range(1,11):
            rezilta=tab*i
            print(f"{tab} x {i} = {rezilta}")
            
    else:
        print("nonb saa enkorek")
    chwa= str(input("eske ou vle kontinye (w/n): "))
    if chwa!='w':
        kontinye=False
        
print("Program nan fini")
    
    