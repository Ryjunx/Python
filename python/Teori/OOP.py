class programs:
    def __init__(self, code, security, log_confict):
        self.code= code
        self.security = security
        self.log_confict = log_confict 
        print(f"os '{self.code}' os applied as sudo...")

    def program_execute(self, hack):
        print(f"{self.code} located conflicting -- malware {hack.code}... \n values_securty  : {self.security}.... \n security execute with code 1")

    def after_execute(self):
        print(f"log. {self.code} -- % value = {self.log_confict} ")


print("ls ~/.")
program = programs(code="home/User/Application/anti.virus.pkg", security="Efective", log_confict="0x82746732t")
malware = programs(code="-w3rh-0-***uhw4.exe", security="none", log_confict="your laptop got hack") 


# print("sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia***sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia*** sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia***sefkgsyefvsfduesyfd=aeyfayiwdyia***sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia*** \nsefkgsyefvsfduesyfd=aeyfayiwdyia*** \nsefkgsyefvsfduesyfd=aeyfayiwdyia*** \n")
malware.program_execute(program)

# print("sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia***sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia*** sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia***sefkgsyefvsfduesyfd=aeyfayiwdyia***sefkgsyefvsfduesyfd=aeyfayiwdyia*** \n sefkgsyefvsfduesyfd=aeyfayiwdyia*** \nsefkgsyefvsfduesyfd=aeyfayiwdyia*** \nsefkgsyefvsfduesyfd=aeyfayiwdyia*** \n")
malware.after_execute()