import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
def agregar_reserva():
    nombre_cliente = entry_nombre.get().strip()
    fecha = entry_fecha.get().strip()
    hora = entry_hora.get().strip()
    if fecha != "" and hora != "":
        item = f"Nombre: {nombre_cliente}, Fecha : {fecha}, Hora : {hora}"
        if item not in lista_reservas.get(0,tk.END):
            lista_reservas.insert(tk.END,item)
            entry_nombre.delete(0,tk.END)
            entry_fecha.delete(0,tk.END)
            entry_hora.delete(0,tk.END)
        else:
            messagebox.showwarning(
                "Error, Ya existe una reserva para esa fecha"
            )

    else:
        messagebox.showerror(
            "Error, La fecha y la hora no pueden estar vacios"
        )

def eliminar_reserva():
    seleccionado = lista_reservas.curselection()
    if seleccionado:
        lista_reservas.delete(seleccionado)
        entry_nombre.delete(0,tk.END)
        entry_fecha.delete(0,tk.END)
        entry_hora.delete(0,tk.END)
    else:
        messagebox.showwarning(
            "Error debes seleccionar una reserva para eliminar"
        )
def actualzar_reserva():
    nombre_cliente = entry_nombre.get().strip()
    fecha = entry_fecha.get()
    hora = entry_hora.get().strip()

    if nombre_cliente != "" and fecha != "" and hora != "":
        nuevo_item = f"Nombre: {nombre_cliente}, Fecha : {fecha}, Hora : {hora}"
        seleccionado = lista_reservas.curselection()
        if seleccionado:
            lista_reservas.delete(seleccionado)
            lista_reservas.insert(seleccionado,nuevo_item)
        else:
            messagebox.showwarning(
                "Error debes seleccionar una reserva para poder actualizar"
            )
    else:
        messagebox.showwarning(
            "Error, No dejar campos vacios"
        )
def obtener_reservas(item):
    partes = item.split(", ")
    nombre = partes[0].split(": ")[1]
    fecha = partes[1].split(": ")[1]
    hora = partes[2].split(": ")[1]
    return nombre, fecha, hora


if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("App Reservas")

    frame_datos = tk.Frame(ventana)
    frame_datos.place(x=20, y=20)

    label_nombre = tk.Label(frame_datos, text="Nombre cliente:")
    label_nombre.grid(row=0, column=0)
    entry_nombre = tk.Entry(frame_datos)
    entry_nombre.grid(row=0, column=1)

    label_fecha = tk.Label(frame_datos, text="Fecha:")
    label_fecha.grid(row=1, column=0)
    entry_fecha = tk.Entry(frame_datos)
    entry_fecha.grid(row=1, column=1)
    frame_datos.pack()

    label_hora = tk.Label(frame_datos, text="Hora")
    label_hora.grid(row=2,column=0)
    entry_hora = tk.Entry(frame_datos)
    entry_hora.grid(row=2,column=1)
    frame_datos.pack()

    frame_botones = tk.Frame(ventana)
    frame_botones.place(x=20, y=130)

    boton_agregar = tk.Button(
        frame_botones, text="Agregar", command=agregar_reserva)
    boton_agregar.pack()

    boton_eliminar = tk.Button(
        frame_botones, text="Eliminar", command=eliminar_reserva)
    boton_eliminar.pack()

    boton_actualizar = tk.Button(
        frame_botones, text="Actualizar", command=actualzar_reserva)
    boton_actualizar.pack()

    frame_botones.pack()

    frame_lista = tk.Frame(ventana)
    frame_lista.place(x=20, y=220)

    lista_reservas = tk.Listbox(frame_lista, width=50, height=10)
    lista_reservas.pack()
    frame_lista.pack()
    ventana.mainloop()