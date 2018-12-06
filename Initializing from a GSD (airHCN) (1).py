#!/usr/bin/env python
# coding: utf-8

# In[25]:


import hoomd
import numpy
import hoomd.md
import sys
import gsd
import gsd.hoomd
hoomd.context.initialize("")


# In[26]:


import mbuild as mb
box = mb.load("/home/themotivation/Avo_atoms/airHCN.pdb")
box.save("/home/themotivation/Avo_atoms/airHCN.gsd")
print("it worked!")


# In[27]:


system = hoomd.init.read_gsd("/home/themotivation/Avo_atoms/airHCN.gsd")


# In[28]:


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


# In[29]:


snap2 = hoomd.data.make_snapshot(N=19904, box=hoomd.data.boxdim(L=100), particle_types=['AR', 'C', 'H', 'N', 'O'])
for x in range(0, 19904):
    snap2.particles.position[x] = snap.particles.position[x]

print(snap2.particles.position)


# In[30]:


print(snap2.particles.position)


# In[31]:


print(snap2.particles.velocity)


# In[32]:


hoomd.init.read_snapshot(snap2);


# In[33]:


nl = hoomd.md.nlist.cell();


# In[34]:


lj = hoomd.md.pair.lj(r_cut=2.5, nlist=nl);


# In[35]:


lj.pair_coeff.set('N','N', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','0', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','AR', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','H', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','C', epsilon=1.0, sigma=1.0);

lj.pair_coeff.set('O','O', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('O','AR', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('O','C', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('O','H', epsilon=1.0, sigma=1.0);

lj.pair_coeff.set('AR','AR', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('AR','H', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('AR','N', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('AR','C', epsilon=1.0, sigma=1.0);

lj.pair_coeff.set('H','C', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('C','C', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('H','H', epsilon=1.0, sigma=1.0);
lj.pair_coeff.set('N','O', epsilon=1.0, sigma=1.0);


# In[36]:


hoomd.md.integrate.mode_standard(dt=0.005);


# In[37]:


all = hoomd.group.all();

integrator = hoomd.md.integrate.npt(group=all, kT=2.49433795843, tau=138.08, tauP=1.0, P=2.0)

integrator.randomize_velocities(seed=42)


# In[38]:


#hoomd.md.integrate.npt(all, kT=2.49433795843, tau=138.08, S=None, P=None, tauP=1, couple='xyz', x=True, y=True, z=True, xy=False, xz=False, yz=False, all=False, nph=False, rescale_all=None, gamma=None)


# hoomd.dump.gsd("trajairHCN.gsd", period=2e3, group=all, overwrite=True);

# In[70]:


hoomd.dump.gsd(filename="trajairHCN.gsd", period=100, group=all, overwrite=True, truncate=False, dynamic=['momentum']);


# In[71]:


hoomd.run(1e4);


# In[72]:


box.save("/home/themotivation/Avo_atoms/trajairHCN.gsd")
print("it worked!")


# In[73]:


hoomd.data.gsd_snapshot("/home/themotivation/Avo_atoms/trajairHCN.gsd", frame=0)


# In[75]:


print(snap.particles.velocity)
print(hoomd.get_step())


# In[ ]:





# In[3]:


snap2 = hoomd.data.make_snapshot(N=19904, box=hoomd.data.boxdim(L=100), particle_types=['AR', 'C', 'H', 'N', 'O'])
for x in range(0, 19904):
    snap3.particles.velocity[x] = "trajairHCN.gsd".particles.velocity[x]


# In[ ]:





# In[ ]:




