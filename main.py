S='eJwrTwIAAVIA2g=='
I=open
H=exit
C=print
import zlib as A,base64 as B,os as G,requests as D
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzjUgACXQWP0EhXP4UQD39HTwUPIA5xdAaKZpSUFBRb6etnlFam5pVk5CdmZiRmliQm6yVl5uvlZOZlc3EBACjSExg='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FVwd/R1VTgy4dj6h7sXOSsEeBxuDFEICfJ8uLvJT8Hp4e55nkCxUGcnR6dIoGLfUEeFYP/QIGdXBR/Pw11+Ch4Pd7cpRDn6+CsAlQLF/LwVnEDiLiDzZnkqcHEBAI0mJhI='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwBNADL/yAgICAtIEtFWSBT4busIEThu6RORyBIVVnhu4BOIFRIT+G6oEkgSOG6okkgVOG6tkMgCgoINBTk'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FXwyczLVvAtTVTwTq1UUFMIyTi8JS9dISQzTyHs4e5GBffE3FQFKy4uADUvDjw='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUACBjJKSgmIrff2M0srUvJKM/MTMjMTMksRkvaTMfL2czLxsLi4AD48NjA=='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FWI8PRTCAw9PFfB2+Nwo7OHQliop4LP4Ul+7grOHg93LYhU8HX09NMLiFQ4MuHh7i4/DwXvwz1gdpOC88NdawIU/IDK1oQohHgcW/9w9xygvojQyMNdfgohQYcbgcp9Hu6e5snFBQDkjixL'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxTUFBQ0FXwONwcqRDi4eir4O7pqODkH6EQ5ejjr3BkwsPdTQp+Hg93rfEDco6tf7h7kTNQ3eEpfu4KIZ5+Ck4Pdy3yU3AGygdAlIUouD/ctcwPzFkSAqQOdypwcQEAohoo9g=='))
T=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLKCkpKLbS108syNRNyi/Ry8/LycxLBXH1y4z1s1Mri/VKKkoADVMN5Q==')
U=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLKCkpKLbS108syNRNyi/Ry8/LycxLBXH1y4z1y1KLijPz8/RKKkoAOjEPLw==')
J=(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrSy0qzszPi8/MS8vXK6koAQA5Ewag')
P=(lambda s:A.decompress(B.b64decode(s)).decode())('eJzLKCkpKLbS108syNRNyi/Ry8/LycxLBXH1y4z1i0rz9AoqAfH2DQc=')
F=(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrKs3TK6gEAAiWAm0=')
if G.path.exists(J):
	with I(J,(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrAgAAcwBz'))as K:L=K.read().strip()
else:L=(lambda s:A.decompress(B.b64decode(s)).decode())('eJwz1DPQMwAAAs4A7g==')
try:V=D.get(T);Q=V.text.strip()
except D.RequestException as E:C(f"Không thể tải key. Lỗi: {E}");H(1)
if not Q:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzzji8JS9doSTj4e5mhZKHuxZnKmSnVuopeGcCBXIVSooSFXIe7lqYqXBk4rEND3fPBapNebhrdZ5CRv7DXduTFbIf7tpfopD3cPfETIVcoMK8dD0AvToqCw=='));H(1)
W=Q.splitlines()
while True:
	R=input((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzy3i4a22BQnZqpcKRiQ93NyuUZD7ctb9AoeTh7qXJCsmHF2SCxHdtL1GwUgAAApAWbw==')).strip()
	if R==(lambda s:A.decompress(B.b64decode(s)).decode())('eJwDAAAAAAE='):C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzTq1UyM44vCUvXeHIxGMbHu5enAxkPNzdrFBS9HD3xLx0PYWw0kyFnMObgCryMh7uWlugkPNw18JMPQBbvBz3'));continue
	if R not in W:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzj8k6tVMjOOLwlL13hyMTDu/LSdRTKSjMVcg5vAorkZB5elaeQ8XB3u0JiSm5mnkJuaaJCdmqlHgCYhxdO'))
	else:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzTq1UODLh8K68dJ0jExLz0hWcMx7uWlip4J6Ym6oIAMpiDOE='));break
try:
	X=D.get(U);M=X.text.strip();C(f"\nPhiên bản hiện tại: {L}");C(f"Phiên bản mới nhất: {M}")
	if L!=M:
		C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzjCsjIPLwqTyHp4a7FeQq5D3fPzlQ4MvHwYoXkw5sVih/u2pqnqHBkQmJeukLJw90bgVIPd88EcpIf7lpboJCXAaRK9PT0AN8EIyk='))
		if G.path.isfile(F):G.remove(F);C((lambda s:A.decompress(B.b64decode(s)).decode())('eJw7MuHwYoWKw5sTFdIyc1IVko+u1AMAYjMJCQ=='))
		C((lambda s:A.decompress(B.b64decode(s)).decode())('eJw7MiExL12h5OGuxZkKBRmZh1flKSQBOXkKuQ93z87U09MDABhyD+c='))
		try:
			N=D.get(P)
			with I(F,(lambda s:A.decompress(B.b64decode(s)).decode())(S))as O:O.write(N.content)
			C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzfrhrbYFCXgaQKlEoyTi8IC9DIfnwlrx0RYWAjMzDq/IUkh7uWpynkPtw9+xMhSMTDy8GEsc2PNy9OFmhBCiTqQcAWiYiGw=='))
			with I(J,(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrBwAAeAB4'))as K:K.write(M)
			C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLyTi8JS9doSQzT6EgI/PwqjyFpIe7FucpHJl4eDGQOLbh4e7FyQrJD3etLVDIywBSJXoK3hkPd8/PBMo+3D0TqDfn4a6FmQrJGcc2HFsIMqro8Jq8DLBss0Lxw91rFVIe7l4KlEAxP/fh7tmZegAX+UE/'));H(0)
		except D.RequestException as E:C(f"Tải file thất bại! Lỗi: {E}");H(1)
except D.RequestException as E:C(f"Không thể kiểm tra phiên bản mới. Lỗi: {E}")
if not G.path.isfile(F):
	C((lambda s:A.decompress(B.b64decode(s)).decode())('eJw7MiExL12h5OGuxZkKaZk5qQp6enoAY2AIMA=='))
	try:
		N=D.get(P)
		with I(F,(lambda s:A.decompress(B.b64decode(s)).decode())(S))as O:O.write(N.content)
		C((lambda s:A.decompress(B.b64decode(s)).decode())('eJwLebhrcaZCWmZOqkJJxuEFeRkKyYe35KUrAgCNOwrh'))
	except D.RequestException as E:C(f"Tải file thất bại! Lỗi: {E}");H(1)
else:C((lambda s:A.decompress(B.b64decode(s)).decode())('eJxzy8xJVTgy8fBihZKHuyfnAcldCzN1FLIzDm/JS1dIfrhrOVhscaZCDkhGDwBCPRf+'))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJzzTq1UODLx8K68dEWFIxMS89IVkjMe7lpYqZCWmZOqp6cHAO5+DaY='))
C((lambda s:A.decompress(B.b64decode(s)).decode())('eJw7MiExL13BO+Ph7vmZCkcmPNw9E8gNTi0qSy3SAwDKcw1F'))
G.system(f"python {F}")
