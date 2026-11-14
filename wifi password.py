import subprocess
def get_wifi_profiles():
    try:
        result = subprocess.check_output(["netsh","wlan","show","profiles"],text=True,
                                         encoding="utf-8",errors="replace")
        names = []
        for line in result.splitlines():
            if "All User Profile" in line:
                name = line.split(":",1)[1].strip()
        if not names:
            print("No saved Wi-Fi profiles found.")
            return
        print("\nSaved Wi-Fi Profiles:\n")
        for i, name in enumerate(names,1):
            print(f"[{i}] {name}")

    except subprocess.CalledProcessError as e:
        print("Error:",e)
    except Exception as e:
        print("Unexpected error:",e)

get_wifi_profiles()
