import tkinter as tk
import tkinter.ttk as ttk
import subprocess
import threading
import os

current_directory = os.getcwd()
file_path=current_directory
path = os.path.join(file_path, "RFmodel.py")

root = tk.Tk()
root.title("Ozone Forecasting App")

status_var = tk.StringVar()
status_bar = ttk.Label(root, textvariable=status_var)
status_bar.pack(side="bottom", fill="x")

def download():
    def run_download_script():
        status_var.set("Downloading Model Data...")
        subprocess.call(["python", str(file_path)+"/experimentalmodel.py"])
        download_complete()
        
    def download_complete():
        # Stop the progress bar animation
        progress_bar.stop()
        status_var.set("Complete")
        
        # Update the GUI to show the download is complete
    # Start the download process in a separate thread
    download_thread = threading.Thread(target=run_download_script)
    download_thread.start()
    
    # Create the progress bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
    progress_bar.pack()
    
    # Start the progress bar animation
    progress_bar.start()
    
    

def processing():
    # Run the processing script in the background using subprocess
    def runprocess():
        status_var.set("Processing NAM Upper Air Data...")
        subprocess.call(["python", str(file_path)+"/model.py"])
        status_var.set("Processing NBM Surface Data...")
        subprocess.call(["python", str(file_path)+"/nbmloop.py"])
        status_var.set("Generating Meteograms")
        subprocess.call(["python", str(file_path)+"/data.py"])
        process_complete()
    def process_complete():
        # Stop the progress bar animation
        progress_bar.stop()
        status_var.set("Complete. See *Data* directory for files")
    process_thread = threading.Thread(target=runprocess)
    process_thread.start()
    
    # Create the progress bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
    progress_bar.pack()
    
    # Start the progress bar animation
    progress_bar.start()
    
def submit():
    ozone1 = float(entry1.get())
    ozone2 = float(entry2.get())
    ozone3 = float(entry3.get())
    ozone4 = float(entry4.get())
    ozone5 = float(entry5.get())
    ozone6 = float(entry6.get())
    cmd = f"python {path} {ozone1} {ozone2} {ozone3} {ozone4} {ozone5} {ozone6}"
    subprocess.run(cmd, shell=True)

    
#def forecast():
#    status_var.set("Computing...")
#    #subprocess.Popen(["python", "RFmodel.py"])
#    #cmd = f"python RFmodel.py {ozone1} {ozone2} {ozone3} {ozone4} {ozone5} {ozone6}"
#    #subprocess.run(cmd, shell=True)
    
download_button = ttk.Button(root, text="Download Data", command=download)
download_button.pack()

#progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
#progress_bar.pack()

processing_button = ttk.Button(root, text="Process Met Files", command=processing)
processing_button.pack()

#forecast_button = ttk.Button(root, text="Forecast", command=forecast)
#forecast_button.pack()


status_label = tk.Label(root, text="8 Hour Concentration Initializion:")
status_label.pack()

#SET UP THE ENTRY BOXES
label1 = tk.Label(root, text="Midlands:")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="Upstate:")
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="CSRA:")
entry3 = tk.Entry(root)

label4 = tk.Label(root, text="Pee Dee:")
entry4 = tk.Entry(root)

label5 = tk.Label(root, text="Catawba:")
entry5 = tk.Entry(root)

label6 = tk.Label(root, text="Trident:")
entry6 = tk.Entry(root)

submit_button = tk.Button(root, text="Submit and Run Forecast", command=submit)

label1.pack()
entry1.pack()

label2.pack()
entry2.pack()

label3.pack()
entry3.pack()

label4.pack()
entry4.pack()

label5.pack()
entry5.pack()

label6.pack()
entry6.pack()

submit_button.pack()


root.mainloop()
