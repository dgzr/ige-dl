# Jumat ,- 04-03-2020
# berhentilah mengubah nama author dan banner milik orang lain
# karena itu sangat tydack epick!! 
# Contact facebook : https://fb.me/Ezz.Kun01

import re,requests,json
from os import system
from tqdm import tqdm

m = '\033[1;31m'
k = '\033[1;33m'
h = '\033[1;32m'
b = '\033[1;34m'
ab = '\033[1;30m'
p = '\033[1;37m'

class BuSyetBro:
	def __init__(self):
		self.req = requests.Session()
		self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"}
		self.menu()
	def menu(self):
		system('clear')
		print(f'             {p}[  {h}Author {ab}: {p}Ezz-Kun{h}({p}zen{h}){p} ]')
		print(f'           {p}[{ab} ☩ {h}Tools{ab} :{p} INSTAGRAM DE EL{ab} ☩ {p}]')
		print(f'           {p}────────────────────────────────')
		print(f'{p}~{m}!{p}[{h} Main Menu {p}]')
		print(f'\n{h}[{p}01{h}]{p}► Get Pict Profile')
		print(f'{h}[{p}02{h}]{p}► Get Image Post')
		print(f'{h}[{p}03{h}]{p}► Get Video Post')
		print(f'{h}[{p}04{h}]{p}► Get Many Image Tags (Limit Scroll)')
		print(f'{h}[{p}05{h}]{p}► Get Media With List Url Post')
		chos = int(input(f'\n{h}[{p}#{h}] {p}Choice : '))
		if chos == 1:
			user = input(f'{h}[{p}?{h}] {p}Username (without @) : ')
			gass = self.req.get('https://www.instadp.com/fullsize/'+user,headers=self.header)
			path = input(f'{h}[{p}?{h}] {p}Path Save (ex:/sdcard/) : ')
			print(f'{h}[{p}!{h}] {p}downloading image')
			yosh = self.req.get(re.search(r'class="picture" src="(.*)"',gass.text).group(1), stream=True)
			progres = tqdm(total=int(yosh.headers.get('content-length', 0)), unit='B', unit_scale=True)
			with open(path+user+'.png', 'wb') as f:
				for data in yosh.iter_content(1024):
					progres.update(len(data))
					f.write(data)
			progres.close()
			print(f'{h}[{p}!{h}] {p}Oke File Saved In : {path}')
			input(f'{h}[{p}!{h}] {p}Back')
			self.menu()
		elif chos == 2:
			url = input(f'{h}[{p}?{h}] {p}URL Post : ')
			hem = self.req.get(url).text
			yamaha = re.findall(r"'display\_url'\:\ \'(.*?)'",str(json.loads(re.search(r"_sharedData = (.*)</",hem).group(1).replace(';',''))))
			print(f'{h}[{p}#{h}]{p} {len(yamaha)} Image Retrevied')
			path = input(f'{h}[{p}?{h}] {p}Path Save (ex:/sdcard/) : ')
			for vega in yamaha:
				name = vega.split('?')[-2].split('/')[-1]
				jupiter = self.req.get(vega, stream=True)
				total_size = int(jupiter.headers.get('content-length', 0))
				block_size = 1024
				beat = tqdm(total=total_size, unit='B', unit_scale=True)
				with open(path+name, 'wb') as f:
					for mber in jupiter.iter_content(block_size):
						beat.update(len(mber))
						f.write(mber)
				beat.close()
			print(f'{h}[{p}!{h}] {p}Oke File Saved In : {path}')
			input(f'{h}[{p}!{h}] {p}Back')
			self.menu()
		elif chos == 3:
			bawang = input(f'{h}[{p}?{h}] {p}URL Post : ')
			goreng = self.req.get(bawang).text
			semua = re.findall(r"\'video\_url'\:\ \'(.*?)'",str(json.loads(re.search(r"_sharedData = (.*)</",goreng).group(1).replace(';',''))))
			print(f'{h}[{p}#{h}]{p} {len(semua)} Videos Retrevied')
			path = input(f'{h}[{p}?{h}] {p}Path Save (ex:/sdcard/) : ')
			for capek in semua:
				name = capek.split('?')[-2].split('/')[-1]
				r = self.req.get(capek, stream=True)
				total_size = int(r.headers.get('content-length', 0))
				block_size = 1024
				t=tqdm(total=total_size, unit='B', unit_scale=True)
				with open(path+name, 'wb') as f:
					for data in r.iter_content(block_size):
						t.update(len(data))
						f.write(data)
				t.close()
			print(f'{h}[{p}!{h}] {p}Oke File Saved In : {path}')
			input(f'{h}[{p}!{h}] {p}Back')
			self.menu()
		elif chos == 4:
			tag = input(f'{h}[{p}?{h}] {p}Tag (without #) : ')
			naik = self.req.get('https://www.instagram.com/explore/tags/'+tag).text
			Beat = re.findall(r"'display\_url'\:\ \'(.*?)'",str(json.loads(re.search(r"_sharedData = (.*)</",naik).group(1).replace(';',''))))
			print(f'{h}[{p}#{h}]{p} {len(Beat)} Images Retrevied')
			path = input(f'{h}[{p}?{h}] {p}Path Save (ex:/sdcard/) : ')
			for vega in Beat:
				name = vega.split('?')[-2].split('/')[-1]
				jupiter = self.req.get(vega, stream=True)
				total_size = int(jupiter.headers.get('content-length', 0))
				block_size = 1024
				beat = tqdm(total=total_size, unit='B', unit_scale=True)
				with open(path+name, 'wb') as f:
					for mber in jupiter.iter_content(block_size):
						beat.update(len(mber))
						f.write(mber)
				beat.close()
			print(f'{h}[{p}!{h}] {p}Oke File Saved In : {path}')
			input(f'{h}[{p}!{h}] {p}Back')
			self.menu()
		elif chos == 5:
			nmax = []
			vid = []
			pik = []
			list = open(input('[#] List Url (ex:lis.txt) : ')).read().splitlines()
			for li in list:
				sop = json.loads(re.search(r"_sharedData = (.*)</",self.req.get(li).text).group(1).replace(';',''))
				if 'video_url' in str(sop):
					get_video = re.findall(r"\'video\_url'\:\ \'(.*?)'",str(sop))
					vid.extend(get_video)
					nmax.extend(get_video)
					print(f'[*] {len(vid)} Video Retrevied')
				elif 'video_url' not in str(sop):
					get_pik = re.findall(r"'display\_url'\:\ \'(.*?)'",str(sop))
					pik.extend(get_pik)
					nmax.extend(get_pik)
					print(f'[*] {len(pik)} Photos Retrevied')
				else:
					break
			path = input(f'{h}[{p}?{h}] {p}Path Save (ex:/sdcard/) : ')
			for honda in nmax:
				name = honda.split('?')[-2].split('/')[-1]
				jupiter = self.req.get(honda, stream=True)
				total_size = int(jupiter.headers.get('content-length', 0))
				block_size = 1024
				beat = tqdm(total=total_size, unit='B', unit_scale=True)
				with open(path+name, 'wb') as f:
					for mber in jupiter.iter_content(block_size):
						beat.update(len(mber))
						f.write(mber)
				beat.close()
			print(f'{h}[{p}!{h}] {p}Oke File Saved In : {path}')
			input(f'{h}[{p}!{h}] {p}Back')
			self.menu()
		else:
			exit(f'{h}[{p}!!{h}]{p} Guoblokkkkk')

try:
	BuSyetBro()
except Exception as e:
	print(f'{h}[{p}!{h}] {p}Guoblok :{h} {str(e)} {p}')
