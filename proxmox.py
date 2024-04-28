

# import requests
# import json
# import urllib3

# def send_request(url, method, data, headers=None):
#     if headers is None:
#         headers = {}
#     if method.upper() == "POST":
#         response = requests.post(url, json=data, headers=headers, verify=False)
#     elif method.upper() == "PUT":
#         response = requests.put(url, json=data, headers=headers, verify=False)
#     else:
#         print("Unsupported method.")
#         return None

#     try:
#         response_content = response.json()  # Attempt to parse JSON
#     except ValueError:
#         response_content = response.text  # Fallback to raw text if JSON parsing fails

#     return response_content

# # Suppress InsecureRequestWarning for unverified HTTPS requests
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # Login and get authentication details
# login_response = send_request(
#     url="https://h19.hologate.pro:8006/api2/extjs/access/ticket",
#     method="POST",
#     data={"username": "root", "password": "wtKDbtg8KQrrr7", "realm": "pam", "new-format": "1"}
# )

# cookie = login_response.get('data', {}).get('ticket')
# token = login_response.get('data', {}).get('CSRFPreventionToken')
# headers_with_auth = {"CSRFPreventionToken": token, "Cookie": f"PVEAuthCookie={cookie}"}

# # Clone operation
# clone_source = 168
# newid = 205
# hostname = newid
# clone_response = send_request(
#     url=f"https://h19.hologate.pro:8006/api2/extjs/nodes/Proxmox-VE/lxc/{clone_source}/clone",
#     method="POST",
#     data={"newid": str(newid), "hostname": str(hostname), "target": "Proxmox-VE", "full": "1"},
#     headers=headers_with_auth
# )
# print(clone_response if isinstance(clone_response, str) else json.dumps(clone_response, indent=4))

# import time
# time.sleep(3)

# # Assuming clone was successful, configure the new LXC container
# VE_num_to_config = newid  # Assuming newid is the ID of the cloned container
# rate = 2.5
# ip_last_octet = VE_num_to_config
# subnet_mask = 26
# config_response = send_request(
#     url=f"https://h19.hologate.pro:8006/api2/extjs/nodes/Proxmox-VE/lxc/{VE_num_to_config}/config",
#     method="PUT",
#     data={"net0": f"name=eth0,hwaddr=BC:24:11:0E:8C:FA,bridge=vmbr1,firewall=1,ip=95.217.100.{ip_last_octet}/{subnet_mask},gw=95.217.100.129,rate={rate}"},
#     headers=headers_with_auth
# )
# print(config_response if isinstance(config_response, str) else json.dumps(config_response, indent=4))


# #---------------------------------------------------------------------------------------------------------------------------

# import requests
# import json
# import urllib3
# import time

# def send_request(url, method, data, headers=None):
#     if headers is None:
#         headers = {}
#     if method.upper() == "POST":
#         response = requests.post(url, json=data, headers=headers, verify=False)
#     elif method.upper() == "PUT":
#         response = requests.put(url, json=data, headers=headers, verify=False)
#     else:
#         print("Unsupported method.")
#         return None

#     try:
#         response_content = response.json()  # Attempt to parse JSON
#     except ValueError:
#         response_content = response.text  # Fallback to raw text if JSON parsing fails

#     return response_content

# # Suppress InsecureRequestWarning for unverified HTTPS requests
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # Login and get authentication details
# login_response = send_request(
#     url="https://h19.hologate.pro:8006/api2/extjs/access/ticket",
#     method="POST",
#     data={"username": "root", "password": "wtKDbtg8KQrrr7", "realm": "pam", "new-format": "1"}
# )

# cookie = login_response.get('data', {}).get('ticket')
# token = login_response.get('data', {}).get('CSRFPreventionToken')
# headers_with_auth = {"CSRFPreventionToken": token, "Cookie": f"PVEAuthCookie={cookie}"}

# # Loop through the new IDs
# for newid in range(207, 211):  # 203 to 220 inclusive
#     clone_source = 168
#     hostname = newid
#     # Clone operation
#     clone_response = send_request(
#         url=f"https://h19.hologate.pro:8006/api2/extjs/nodes/Proxmox-VE/lxc/{clone_source}/clone",
#         method="POST",
#         data={"newid": str(newid), "hostname": str(hostname), "target": "Proxmox-VE", "full": "1"},
#         headers=headers_with_auth
#     )
#     print(f"Clone response for newid={newid}:", clone_response if isinstance(clone_response, str) else json.dumps(clone_response, indent=4))

#     time.sleep(5)
    
#     # Assuming clone was successful, configure the new LXC container
#     VE_num_to_config = newid
#     rate = 2.5
#     ip_last_octet = VE_num_to_config
#     subnet_mask = 26
#     config_response = send_request(
#         url=f"https://h19.hologate.pro:8006/api2/extjs/nodes/Proxmox-VE/lxc/{VE_num_to_config}/config",
#         method="PUT",
#         data={"net0": f"name=eth0,hwaddr=BC:24:11:0E:8C:FA,bridge=vmbr1,firewall=1,ip=95.217.100.{ip_last_octet}/{subnet_mask},gw=95.217.100.129,rate={rate}"},
#         headers=headers_with_auth
#     )
#     print(f"Config response for newid={newid}:", config_response if isinstance(config_response, str) else json.dumps(config_response, indent=4))
#     time.sleep(5)



#-----------------------------------------------------------------------------------------------------------------------
import requests
import json
import urllib3
import time

def send_request(url, method, data, headers=None):
    if headers is None:
        headers = {}
    try:
        if method.upper() == "POST":
            response = requests.post(url, json=data, headers=headers, verify=False)
        elif method.upper() == "PUT":
            response = requests.put(url, json=data, headers=headers, verify=False)
        else:
            print("Unsupported method.")
            return None, True  # Return an error occurred

        response.raise_for_status()  # Raises stored HTTPError, if one occurred
        try:
            response_content = response.json()
        except ValueError:
            response_content = response.text
        return response_content, False  # Return no error occurred
    except requests.exceptions.HTTPError as err:
        return str(err), True  # Return an error occurred

# Suppress InsecureRequestWarning for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Login and get authentication details
login_response, error = send_request(
    url="https://h19.hologate.pro:8006/api2/extjs/access/ticket",
    method="POST",
    data={"username": "root", "password": "wtKDbtg8KQrrr7", "realm": "pam", "new-format": "1"}
)
if error:
    print("Login failed:", login_response)
    exit()  # Stop execution if login fails

cookie = login_response.get('data', {}).get('ticket')
token = login_response.get('data', {}).get('CSRFPreventionToken')
headers_with_auth = {"CSRFPreventionToken": token, "Cookie": f"PVEAuthCookie={cookie}"}

# Iterate through new IDs
for newid in range(231, 241):
    hostname = newid
    VE_num_to_config = newid
    rate = 2.5
    ip_last_octet = VE_num_to_config
    subnet_mask = 26

    # Clone operation
    clone_response, error = send_request(
        url=f"https://h19.hologate.pro:8006/api2/extjs/nodes/Proxmox-VE/lxc/168/clone",
        method="POST",
        data={"newid": str(newid), "hostname": str(hostname), "target": "Proxmox-VE", "full": "1"},
        headers=headers_with_auth
    )
    if error:
        print(f"Error cloning container with newid {newid}:", clone_response)
        continue  # Skip to the next ID or consider exiting based on your needs

    print(f"Clone operation successful for newid {newid}:", clone_response)
    time.sleep(5)

    # Config operation
    config_response, error = send_request(
        url=f"https://h19.hologate.pro:8006/api2/extjs/nodes/Proxmox-VE/lxc/{VE_num_to_config}/config",
        method="PUT",
        data={"net0": f"name=eth0,hwaddr=BC:24:11:0E:8C:FA,bridge=vmbr1,firewall=1,ip=95.217.100.{ip_last_octet}/{subnet_mask},gw=95.217.100.129,rate={rate}"},
        headers=headers_with_auth
    )
    if error:
        print(f"Error configuring container with newid {newid}:", config_response)
        continue  # Skip to the next ID or consider exiting based on your needs

    print(f"Config operation successful for newid {newid}:", config_response)
    time.sleep(5)


