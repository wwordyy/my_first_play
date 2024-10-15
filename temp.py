balance = 200

market = [{
    1:{"1. Плюшевый мишка" : "100$",
    "2. Духи Dior" : "200$",
    "3. Холодильник Samsug" : "300$",
    },
    2:{"4. Яндекс Алиса" : "400$",
    "5. Playstation 5" : "500$",
    "6. Ноутбук HONOR" : "600$",
    },
    3:{"7. Iphone 14" : "700$",
    "8. Macbook Pro" : "800$",
    "9. Iphone 16" : "900$" ,
    },    
}]

if balance > 0:
            print("Добро пожаловать в наш магазин, здесь вы можете купить товар на выигранные деньги.")
            temp = market[0][1]
 
            for key, value in temp.items():
                print(f"{key} -- {value}")

while True:
            print()
            print("Выберите предмет который хотите купить. Для выхода из магазина да введите 0.")
            user = input()
                
            if user == "Плюшевый мишка" or user == "1":
                print(f"Спасибо вам за покупку :). Ваш баланс:  {balance - 100} $")
                break
                

            elif user == "Духи Dior" or user == "2":
                 
                    if balance < 200:
                        print("Недостаточно средств! Выберите другой предмет.")
                        break
                    else:
                        print(f"Спасибо вам за покупку :). Ваш баланс:  {balance - 200} $")
                        break
                
            
            
                    

            elif user == "Холодильник Samsug" or user == "3":
                while True:
                    if balance < 300:
                        print("Недостаточно средств! Выберите другой предмет.")
                        break

                    else:
                        print(f"Спасибо вам за покупку :). Ваш баланс:  {balance - 300} $")
                        break
                continue
                    

            elif user == "0":
                print(f"Ваш баланс:  {balance} $. Спасибо вам за игру :)")
                break
                

            else:
                print("Эххх, непонятное значение!")
                    
else:
    print("Удачи на дорогах, не растраивайтесь :)")