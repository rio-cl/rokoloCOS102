def reciept():
    selected_option = food_var.get()
    price = food_prices[selected_option]
    messagebox.showinfo("Option Selected", f"You selected: {selected_option}\nPrice: ₦{price:.2f}")

for food_item, price in food_prices.items():
    label = tk.Label(root, text=f"{food_item}: ₦{price:.2f}")
    label.pack()

    food_var = tk.StringVar(root)