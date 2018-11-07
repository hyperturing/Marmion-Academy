#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hoomd
import numpy
import hoomd.md 
import sys
import gsd
import gsd.hoomd
hoomd.context.initialize("")


# In[2]:


import mbuild as mb
box = mb.load("/home/themotivation/Avo_atoms/airHCN.pdb")
box.save("/home/themotivation/Avo_atoms/airHCN.gsd")
print("it worked!")


# In[3]:


system = hoomd.init.read_gsd("/home/themotivation/Avo_atoms/airHCN.gsd")


# In[3]:


#first line opens the gsd file so hoomd can read it. second line specifies the first (and only) frame of the gsd file (this gsd . 
#third line  confirms frame. 
#fourth line shows us the type/name of particles (atoms/molecules) that hoomd recognizes
#fifth line shows us the snapshot at the specified timestep in the gsd file

t = gsd.hoomd.open(name='/home/themotivation/Avo_atoms/airHCN.gsd', mode='rb')
snap = t[0]
snap.configuration.step
print(snap.particles.types)
print(snap.particles.position)
#snap.particles.particle_types
#snap.particles.position


# In[4]:


snap2 = hoomd.data.make_snapshot(N=19904, box=hoomd.data.boxdim(L=100), particle_types=['AR', 'C', 'H', 'N', 'O'])
for x in range(0, 19904):
    snap2.particles.position[x] = snap.particles.position[x]

print(snap2.particles.position)


# In[5]:


print(snap2.particles.position)


# In[6]:


print(snap2.particles.velocity)


# In[6]:


hoomd.init.read_snapshot(snap2);


# In[ ]:





# In[7]:


nl = hoomd.md.nlist.cell();


# In[8]:


lj = hoomd.md.pair.lj(r_cut=2.5, nlist=nl);


# In[9]:


lj.pair_coeff.set('N','N', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','0', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','AR', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','H', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','C', epsilon=1.0, sigma=1.0);

lj.pair_coeff.set('O','O)', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('O','AR', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('O','C', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('O','H', epsilon=1.0, sigma=1.0);

lj.pair_coeff.set('AR','AR)', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('AR','H', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('AR','N', epsilon=1.0, sigma=1.0);

lj.pair_coeff.set('H','C)', epsilon=1.0, sigma=1.0);


# In[10]:


hoomd.md.integrate.mode_standard(dt=0.005);


# In[11]:


snap2 = hoomd.group.all();
hoomd.md.integrate.langevin(group=all, kT=0.2, seed=42);


# In[12]:


print(snap2.particles.position)


# In[ ]:




