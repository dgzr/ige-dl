#coding=utf-8
# Jumat ,- 04-03-2020
# berhentilah mengubah nama author dan banner milik orang lain
# karena itu sangat tydack epick :v
# facebook : https://fb.me/Ezz.Kun01
import re,requests,json
from os import system
from tqdm import tqdm

m = '\033[1;31m'
k = '\033[1;33m'
h = '\033[1;32m'
b = '\033[1;34m'
ab = '\033[1;30m'
p = '\033[1;37m'

class boring:
	def __init__(self):
		self.req = requests.Session()
		self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"}
		self.menu()
	def menu(self):
		system('clear')
		print('             %s[  %sAuthor %s: %sEzz-Kun%s(%szen%s) %s]'%(p,h,ab,p,h,p,h,p))
		print('           %s[ %s☩ %sTools %s: %sINSTAGRAM DE EL %s☩ %s]'%(p,ab,h,ab,p,ab,p))
		print('           ────────────────────────────────')
		print('%s~%s!%s[ %sMain Menu %s]'%(p,m,p,h,p))
		print('\n%s{%s01%s}%s► Get Pict Profile'%(h,p,h,p))
		print('%s{%s02%s}%s► Get Image Post'%(h,p,h,p))
		print('%s{%s03%s}%s► Get Video Post'%(h,p,h,p))
		print('%s{%s04%s}%s► Get Many Image Tags (Limit Scroll)'%(h,p,h,p))
		chos = int(input('\n%s[%s?%s] Choice %s:%s '%(p,h,p,ab,p)))
		if chos == 1:
			user = input('%s[%s?%s] Username %s:%s '%(p,h,p,ab,p))
			gass = self.req.get('https://www.instadp.com/fullsize/'+user,headers=self.header)
			cari = re.search(r'class="picture" src="(.*)"',gass.text).group(1)
			name = re.search(r"\d_.*.jpg.*?",cari).group(0)
			path = input('%s[%s?%s] Path Save (ex:/sdcard/) : '%(p,h,p))
			print('%s[%s!%s] downloading image'%(p,h,p))
			yosh = self.req.get(cari, stream=True)
			total_size = int(yosh.headers.get('content-length', 0))
			block_size = 1024
			progres = tqdm(total=total_size, unit='B', unit_scale=True)
			with open(path+name, 'wb') as f:
				for data in yosh.iter_content(block_size):
					progres.update(len(data))
					f.write(data)
			progres.close()
			print('%s[%s!%s] Oke File Saved In %s: %s%s'%(p,h,p,ab,p,path))
			input('%s[%s?%s] Back'%(p,h,p))
		elif chos == 2:
			url = input('%s[%s?%s] Url Post %s:%s '%(p,h,p,ab,p))
			hem = self.req.get(url).text
			ntah = re.search(r"_sharedData = (.*)</",hem).group(1).replace(';','')
			yamaha = re.findall(r"'display\_url'\:\ \'(.*?)'",str(json.loads(ntah)))
			print('%s[%s!%s] %s Image Retrevied'%(p,h,p,len(yamaha)))
			path = input('%s[%s?%s] Path Save (ex:/sdcaard) %s:%s '%(p,h,p,ab,p))
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
			print('%s[%s!%s] Oke File Saved In %s: %s%s'%(p,h,p,ab,p,path))
			input('%s[%s?%s] Back'%(p,h,p))
			self.menu()
		elif chos == 3:
			bawang = input('%s[%s?%s] Url Post %s:%s '%(p,h,p,ab,p))
			goreng = self.req.get(bawang).text
			enak = re.search(r"_sharedData = (.*)</",goreng).group(1).replace(';','')
			semua = re.findall(r"\'video\_url'\:\ \'(.*?)'",str(json.loads(enak)))
			print('%s[%s!%s] %s videos Retrevied'%(p,h,p,len(semua)))
			path = input('%s[%s?%s] Path Save (ex:/sdcaard) %s:%s '%(p,h,p,ab,p))
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
			print('%s[%s!%s] Oke File Saved In %s: %s%s'%(p,h,p,ab,p,path))
			input('%s[%s?%s] Back'%(p,h,p))
			self.menu()
		elif chos == 4:
			tag = input('%s[%s?%s] Tags (without:#) %s:%s '%(p,h,p,ab,p))
			hem = self.req.get('https://www.instagram.com/explore/tags/'+tag).text
			ntah = re.search(r"_sharedData = (.*)</",hem).group(1).replace(';','')
			yamaha = re.findall(r"'display\_url'\:\ \'(.*?)'",str(json.loads(ntah)))
			print('%s[%s!%s] %s Image Retrevied'%(p,h,p,len(yamaha)))
			path = input('%s[%s?%s] Path Save (ex:/sdcaard) %s:%s '%(p,h,p,ab,p))
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
			print('%s[%s!%s] Oke File Saved In %s: %s%s'%(p,h,p,ab,p,path))
			input('%s[%s?%s] Back'%(p,h,p))
			self.menu()
		else:
			exit('%s[%s!%s] Goublokklklllkkl'%(p,m,p))
try:
	boring()
except Exception as e:
	print('%s[%s!%s] wrong %s: %s%s'%(p,m,p,ab,m,str(e)))
