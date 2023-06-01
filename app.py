import tkinter as tk
from tkinter import ttk
import re

COMPONENTS = ['Engine', 'Gearbox', 'Tires', 'Wings']
CONFIGURATIONS = ['Tejas', 'Rudra', 'Dhruv', 'AMCA']

TRANSCRIPT_FILE = open(r"D:\ASBA_HAL\res\transcriptionData")
TRANSCRIPTION_DATA = TRANSCRIPT_FILE.read()
print(TRANSCRIPTION_DATA)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Root window configuration
        self.title('HAL ASBA')
        self.geometry('600x600')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)

        # Components
        # Panels
        # Music Player Frame - Stores the music player and options to load, convert audio etc
        musicPlayerFrame = tk.Frame(self, bg='black')
        musicPlayerFrame.grid(row=0, column=0, padx=5, pady=2, sticky='nsew')

        # Content Frame - Body frame containing config, reportHistory, report and transcript frame
        contentFrame = tk.Frame(self, bg='red')
        contentFrame.grid(row=1, column=0, padx=5, pady=2, sticky='nsew')

        # Config and Report History Frame - Contains config frame and report history frame
        contentFrame.rowconfigure(0, weight=1)
        contentFrame.columnconfigure(0, weight=1)
        settingsFrame = tk.Frame(contentFrame, bg='yellow')
        settingsFrame.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

        # Report Frame - Contains the current generated report
        contentFrame.columnconfigure(1, weight=5)
        reportFrame = tk.Frame(contentFrame, bg='violet')
        reportFrame.grid(row=0, column=1, padx=2, pady=2, sticky='nsew')

        # Transcript Frame - Contains the transcript generated from audio
        contentFrame.columnconfigure(2, weight=1)
        transcriptFrame = tk.Frame(contentFrame, bg='green')
        transcriptFrame.grid(row=0, column=2, padx=2, pady=2, sticky='nsew')

        # Config Frame - Stores preconfigured components options
        settingsFrame.columnconfigure(0, weight=1)
        settingsFrame.rowconfigure(0, weight=1)
        configFrame = tk.Frame(settingsFrame, bg='pink')
        configFrame.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

        # Report History Frame - Stores list of previously generated reports
        settingsFrame.rowconfigure(1, weight=1)
        reportHistoryFrame = tk.Frame(settingsFrame, bg='indigo')
        reportHistoryFrame.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

        # Panel Components

        # Music Player Components
        mpTile = tk.Label(musicPlayerFrame, text='Audio Player')
        mpTile.grid(row=0, column=0, padx=5, pady=2)

        # Config Frame Components
        configTitle = tk.Label(configFrame, text='Configurations')
        configTitle.grid(row=0, column=0, padx=2, pady=2, sticky='nw')

        configFrame.rowconfigure(1, weight=4)
        configFrame.columnconfigure(0, weight=1)
        configList = tk.Listbox(configFrame, font=('Times', 12))
        configList.insert(0, *CONFIGURATIONS)
        configList.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        configFrame.rowconfigure(2, weight=1)
        configBtnFrame = tk.Frame(configFrame)
        configBtnFrame.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        configLoadBtn = tk.Button(configBtnFrame, text="Load")
        configEditBtn = tk.Button(configBtnFrame, text="Edit")
        configDeleteBtn = tk.Button(configBtnFrame, text='Delete')

        configBtnFrame.columnconfigure(0, weight=1)
        configLoadBtn.grid(row=0, column=0, padx=5, pady=2, sticky='nsew')
        configBtnFrame.columnconfigure(1, weight=1)
        configEditBtn.grid(row=0, column=1, padx=5, pady=2, sticky='nsew')
        configBtnFrame.columnconfigure(2, weight=1)
        configDeleteBtn.grid(row=0, column=2, padx=5, pady=2, sticky='nsew')

        # Report History Frame Components
        reportHistoryTitle = tk.Label(reportHistoryFrame, text='Report History')
        reportHistoryTitle.grid(row=1, column=0, padx=2, pady=2)

        # Report Frame Components
        reportFrame.columnconfigure(0, weight=1)

        reportTitle = tk.Label(reportFrame, text='Report')
        reportTitle.grid(row=0, column=0, padx=2, pady=2, sticky='nw')
        reportFrame.rowconfigure(1, weight=1)

        reportBodyFrame = tk.Frame(reportFrame, background='yellow')
        reportBodyFrame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        reportBodyFrame.rowconfigure(0, weight=1)
        reportBodyFrame.columnconfigure(0, weight=1)
        componentList = tk.Listbox(reportBodyFrame, font=('Times', 12))
        componentList.insert(0, *COMPONENTS)
        componentList.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        reportBodyFrame.columnconfigure(1, weight=9)
        componentDescArea = tk.Label(reportBodyFrame, text='Description unavailable', font=('Times', 12),
                                     justify='left', )
        componentDescArea.grid(row=0, column=1, padx=5, pady=5, sticky='nw')

        # Transcript Frame Components
        transcriptFrame.columnconfigure(0, weight=1)
        transcriptTitle = tk.Label(transcriptFrame, text='Transcript')
        transcriptTitle.grid(row=0, column=0, padx=2, pady=2, sticky='nw')

        transcriptFrame.rowconfigure(1, weight=1)
        transcriptionText = tk.Label(transcriptFrame, text=TRANSCRIPTION_DATA, justify='left', wraplength=300,
                                     anchor='nw')
        transcriptionText.grid(row=1, column=0, padx=5, pady=10, sticky='new')


if __name__ == "__main__":
    app = App()
    app.mainloop()
