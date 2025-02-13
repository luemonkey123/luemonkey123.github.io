---
title: New NAS build plan
date: 2025-02-08 21:00:00 -0500
categories:
  - homelab
  - project
tags:
  - NAS
  - project
  - server
  - plan
---

# Idea

Well, today my [cm3588](https://www.friendlyelec.com/index.php?route=product/product&product_id=294) that I use as a NAS failed, so I guess it is time to rethink my decision. Well, first of all, because all that stopped working was the ethernet port, I could just get a cheap usb 3 to 1 gig ethernet adapter on amazon, and go through much google to get drivers working, and while I might do that anyway, I suffer from a bad case of scope creep and decided to do more research. 

# Research

## Settling on a new NAS

### Ideas 

I talked to myself in the shower for ~10 mins and tried to organize my thoughts, and this is basically what I came up with

- Run Jellyfin on a [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) with some external disks and also call it a day
- Try to make the current NAS board work
- Proxmox cluster?
- Proper motherboard and CPU (suggested by my dad)

### Choosing

It was pretty easy to rule out the Jellyfin on the RPI b/c that doesn't really solve the base problem, the NAS, and would get pretty bottlenecked and expensive.

I could try to make the current board work, but I don't think that that solves the root problem. [Armbian](https://www.armbian.com/) is by no means stable, at least not the [CM3588](https://www.armbian.com/nanopc-cm3588-nas/) image. The official ones are no better, with outdated distros and kernal. The m.2 is only gen 3, so that is not the best.

A Proxmox cluster seemed to be a good option, but it would be really expensive. 3x the cost, 3x the power bill, <3x the compute, and a whole lot more reliability. Although it sounded really cool to have 100% uptime, I think that it is not too important for me. I really miss my Jellyfin music server after like a week, but a day or two shouldn't be too bad.

The last option that I finally settled on was the proper motherboard. I was a little worried about the power consumption, as I still am, but that was not a big as the exuberation that I would finally build a computer, my very own.
## Preliminary

After asking my friend Issac about somethings, he said that maybe I should get an intel CPU. I hadn't really thought about that before, because I had heard that AMD's AM4 platform was really upgradable and good value for money. I settled on the i5 raptor lake refresh, or the 14th gen Intel core i5. 

I had wanted to get mini-itx for a while now, for whatever it was I was gonna build, be it a server or a pc. There was just something about ITX that lured me. Maybe it was their tininess and the fact that they're not quite mainstream. Even that aside, the practical use of Mini-ITX in my server would be to fit on a 10" server rack, which I hope to get someday. (Although on Amazon the rack I was gonna get is out of stock? [Huh?](https://www.amazon.com/GeeekPi-Cabinet-Equipment-RackMate-Rackmount/dp/B0CSCWVTQ7?ref_=ast_sto_dp))

I remembered a shelf to hold ITX builds, and that is [this shelf](https://www.amazon.com/dp/B0D5XNDFDZ?tag=pcpapi-20&linkCode=ogi&th=1&psc=1). I'm still not quite sure about power supply mounting, but that is a problem for future me. (This mindset is def a risky way to go about life)

## Choosing Parts

First, my parts list is [here](https://pcpartpicker.com/user/luemonkey123/saved/#view=8mFHRB) on pcpartpicker. It is not quite accurate in that I already have the ssd, the motherboard doesn't have a price, and I think I will get the CPU from a micro-center deal $30 cheaper. 

For the CPU, as mentioned above, I went with the Intel Core i5 14400 raptor lake refresh. It seemed decently power efficient and priced, so that is what I went with. I was originally going to get the i5 14400f, which doesn't have integrated graphics, but my dad informed me that there is also no shell. Plus, an integrated GPU might be helpful in the future (transcoding??).

The motherboard was much harder to choose. My dad wanted me to just build in a normal case, but I really wanted Mini-ITX. There were several options I jumped around on, including [this B760](https://pcpartpicker.com/product/YxLFf7/asus-rog-strix-b760-i-gaming-wifi-mini-itx-lga1700-motherboard-rog-strix-b760-i-gaming-wifi) motherboard and [this one](https://pcpartpicker.com/product/WC6NnQ/gigabyte-b760i-aorus-pro-mini-itx-lga1700-motherboard-b760i-aorus-pro) too. I eventually found [something like this](https://www.newegg.com/p/1JW-00NN-00035). This seemed like very good value for the price, and almost identical to the two above. The only difference seemed to be the not metal reinforced pcie slot and the slow shipping time. These seemed insignificant, so I went through with it.

For the RAM, we just went with any old cheap DDR5, a silicon power [kit](https://pcpartpicker.com/product/scFmP6/silicon-power-xpower-zenith-gaming-32-gb-2-x-16-gb-ddr5-6000-cl30-memory-sp032gxlwu60afde).

The storage was very simple to pick out, because it was picked out by past Evan. It is a WD Blue [drive ](https://pcpartpicker.com/product/rqhv6h/western-digital-blue-sn580-1-tb-m2-2280-pcie-40-x4-nvme-solid-state-drive-wds100t3b0e), just a really cheap one at the time. Luckily for me I decided to spend the extra $2 and get the pcie gen 4 variant.

For the power supply as well, I just went to the [Corsair 750e](https://pcpartpicker.com/product/YRJp99/corsair-rm750e-2023-750-w-80-gold-certified-fully-modular-atx-power-supply-cp-9020262-na), a very popular one and one that my friend Issac also happened to use. Cool!

Then, finally, there is the planned mounting solution. When and if I get a 10" rack, I hope to rack mount it with this tray. I'm not even sure if that's a good idea, because the power supply and drives would take up a lot more rack space, right? Maybe I should just go with a tried and true NAS case. I don't even know, just reasoning to myself as I type. Here is the ITX [mount](https://www.amazon.com/dp/B0D5XNDFDZ?tag=pcpapi-20&linkCode=ogi&th=1&psc=1) anyway.

# Software

## Options

There were a few options that I wanted to explore:

- Unraid also as a docker manager and VM hypervisor
- TrueNAS, also as a docker manager and VM hypervisor
- proxmox running virtualized either Unraid or TrueNAS and more VMs
- ~~Definitely not OMV again~~

I think that I with use TrueNAS, b/c it is free and proxmox requires network shares. That is the plan, I think I will have an update in about a month.

# Conclusion

That's the plan, anyways. I will go to Micro Center on Sat, where I might adjust the plan some to accommodate prices, msrp, etc. This is the pcpartpicker [list](https://pcpartpicker.com/user/luemonkey123/saved/#view=TZBx23).