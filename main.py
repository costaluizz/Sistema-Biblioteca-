from controllers.login_controller import LoginController
import tkinter as tk
def main():
    root = tk.Tk()
    controller = LoginController(root)
    controller.iniciar_login()
    root.mainloop()

if __name__ == "__main__":
    main()