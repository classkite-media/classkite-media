import numpy as np, soundfile as sf, sys
sr=48000; dur=float(sys.argv[2]); bpm=100; beat=60/bpm
N=int(sr*dur); L=np.zeros(N); R=np.zeros(N)
def f(m): return 440*2**((m-69)/12)
prog=[[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,67]]  # Cmaj7 Am7 Fmaj7 G
bar=4*beat
def env(n,a,r):
    e=np.ones(n); ai=min(n,int(a*sr)); ri=min(n,int(r*sr))
    e[:ai]=np.linspace(0,1,ai); e[-ri:]*=np.linspace(1,0,ri); return e
t_bar=np.arange(int(bar*sr))/sr
b=0
while b*bar<dur:
    ch=prog[b%4]; s=int(b*bar*sr); n=min(len(t_bar),N-s)
    pad=sum(np.sin(2*np.pi*f(m-12)*t_bar[:n])*0.5+np.sin(2*np.pi*f(m-12)*1.003*t_bar[:n])*0.5 for m in ch)/len(ch)
    pad*=env(n,0.6,0.6)*0.18
    L[s:s+n]+=pad; R[s:s+n]+=pad
    bass=np.sin(2*np.pi*f(ch[0]-24)*t_bar[:n])*env(n,0.05,0.4)*0.22
    L[s:s+n]+=bass; R[s:s+n]+=bass
    arp=[ch[0]+12,ch[1]+12,ch[2]+12,ch[3]+12,ch[2]+12,ch[1]+12,ch[2]+12,ch[3]+12]
    for k,m in enumerate(arp):
        st=s+int(k*beat/2*sr); ln=int(0.9*sr)
        if st>=N: break
        ln=min(ln,N-st); tt=np.arange(ln)/sr
        tone=(np.sin(2*np.pi*f(m)*tt)+0.3*np.sin(2*np.pi*2*f(m)*tt))*np.exp(-tt*5)*0.10
        pan=0.35 if k%2 else 0.65
        L[st:st+ln]+=tone*(1-pan)*2; R[st:st+ln]+=tone*pan*2
    b+=1
mix=np.stack([L,R],1)
fade=int(1.5*sr); mix[:int(0.5*sr)]*=np.linspace(0,1,int(0.5*sr))[:,None]; mix[-fade:]*=np.linspace(1,0,fade)[:,None]
mix/=np.abs(mix).max()*1.12
sf.write(sys.argv[1],mix,sr)
