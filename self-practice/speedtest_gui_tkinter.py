import tkinter as tk
import speedtest as st

def speed_test():
    #create a speedtest instance
    test = st.Speedtest()

    #perform tests
    download_speed = test.download()
    upload_speed = test.upload()
    ping = test.results.ping

    #convert speed to MBPS

    download_speed_mbps = round(download_speed / 10**6, 2)
    upload_speed_mbps = round(upload_speed / 10**6, 2)

    #upload the label with the speed-test results(label is created with tkinter like below)
    result_label.config(text=f"Download Speed: {download_speed_mbps} Mbps\n"
                              f"Upload Speed: {upload_speed_mbps} Mbps\n"
                              f"Ping: {ping} ms")
#create the main window with Tkinter
root = tk.Tk()
root.title("Internet Speed Test")
#create the button inside root/main window
test_button = tk.Button(root, text="Test your internet speed", command=speed_test)
test_button.pack(pady=20)
#create a label to display results
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)
#start the tkinter event loop
root.mainloop()
