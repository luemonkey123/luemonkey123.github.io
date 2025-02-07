---
title: Bedroom Lights
date: 2025-2-06 19:30:00 -0500
categories:
  - home
  - smart
tags:
  - smart-home
  - project
---

In my bedroom there are no ceiling lights, we bought a smart floor lamp that works with homeassistant. What I didn't think would annoy me so much was that I couldn't turn on the lights when I walked in, because the remote would often be by my bed. We bought [this](https://www.aliexpress.us/item/3256805546087566.html?spm=a2g0o.order_list.order_list_main.145.10231802k91Mho&gatewayAdapt=glo2usa) switch that would work with the tuya integration. 

I had tried to install it when I got it, like 6 months ago, but I was so confused back then. The problem seemed to be which wires were which, what I (correctly) attributed it to being a two switch network. Here is a good image to describe it: ![Image Description](/assets/img/pimg/Pasted%20image%2020250206180911.png)

The real problem was the lack of neutral. When measured across the pins with a multimeter, it would read ~60V AC, even the with the switches in the correct positions. So, what we eventually did was, to get real neutral, to short the outlet together. My initial reaction, which should be yours if you know anything about electronics, is "WTH?" Well, we eventually thought that it would work, at least in theory. So, I got a fire extinguisher, turned off the breaker for that room, and got the wagos. After turning back on the power, somehow nothing exploded or caught fire or tripped a breaker, and THE LIGHT ON THE SWITCH TURNED ON!!! After that, it was pretty simple to just get the software all setup and the automations.![Image Description](/assets/img/pimg/Screenshot%202025-02-06%20at%207.10.39%20PM.png)![Image Description](/assets/img/pimg/Screenshot%202025-02-06%20at%207.11.09%20PM.png)![Image Description](/assets/img/pimg/Screenshot%202025-02-06%20at%207.11.26%20PM.png)
![Image Description](/assets/img/pimg/Screenshot%202025-02-06%20at%207.15.08%20PM.png)

The other two are pretty much just the inverse.