# Keyboard

This project is a 75% mechanical keyboard that I developed from scratch using KiCad. The idea was to create a compact, functional, and relatively simple keyboard, retaining the main keys of a conventional keyboard without taking up too much desk space.
The project was designed to be a real physical keyboard, so I didn't just focus on the visual aspect: I developed the circuit board (PCB), organized the key matrix, defined the electrical connections, and chose the necessary components so that the keyboard can be assembled and used later.

This project was going to be submitted to the Fabricate program, but I decided against it; I'll post it here instead. Because I thought halfway through, I have several other things to do, it's better not to. I didn't end up submitting it!

# Layout 
The keyboard uses a 75% layout, which retains virtually all the important functions of a full keyboard, but eliminates the spacebar and some less frequently used keys.
It has the main letter, number, and symbol keys, as well as keys such as the arrow keys, Shift, Ctrl, Alt, Enter, Backspace, and other function keys.

<img width="1010" height="368" alt="Screenshot_1" src="https://github.com/user-attachments/assets/b0c64295-bfcd-44dc-8839-41335232f39e" />
<img width="1444" height="572" alt="front_pcb" src="https://github.com/user-attachments/assets/3562a8d1-4a6e-404b-bcb3-3663f8fe4406" />


# PCB

The entire board was designed in KiCad. First, I arranged the keys according to the chosen layout and then started working on the electrical part.
The keys are part of a matrix of rows and columns. This way, it's not necessary to connect each key directly to a separate microcontroller pin. Each switch is connected to the matrix, allowing the microcontroller to identify which key was pressed.
I also added the components necessary for the correct reading of the matrix, including the diodes associated with the keys.

<img width="1388" height="540" alt="back_pcb" src="https://github.com/user-attachments/assets/fb5f11a6-8899-4c6a-8105-fc64ea92fd3f" />
<img width="1444" height="572" alt="front_pcb" src="https://github.com/user-attachments/assets/193cbaa0-e3ab-4c72-9146-9b73986189d9" />
<img width="1505" height="543" alt="pcb_editor" src="https://github.com/user-attachments/assets/68224921-2cd4-4391-ac17-4c523486000e" />

# Scheme
<img width="823" height="576" alt="general_scheme" src="https://github.com/user-attachments/assets/ed67c541-1166-4a61-8cd5-39cc680b5e78" />
<img width="801" height="368" alt="matrix" src="https://github.com/user-attachments/assets/418a0b90-6870-4562-aff9-e242011f00fb" />
<img width="394" height="658" alt="mx_stap" src="https://github.com/user-attachments/assets/c5f0386a-b822-470d-b5f7-da5ad212a7c6" />
<img width="847" height="721" alt="raspberrypi" src="https://github.com/user-attachments/assets/2c19bcc0-35dd-44c7-a84c-b253bd622d28" />

# Parts used for the project:

## Raspberry Pi Pico
The keyboard has a microcontroller responsible for reading the key matrix and transforming the keystrokes into commands that the computer can interpret.
<img width="960" height="552" alt="image" src="https://github.com/user-attachments/assets/a6454b8a-7c1e-4d02-84c1-b22a872cb3e8" />

## Diode 1N4148
<img width="1199" height="1200" alt="image" src="https://github.com/user-attachments/assets/77995c7d-b516-4f99-b8ae-6e605004364c" />

## Stabilizers
<img width="528" height="378" alt="image" src="https://github.com/user-attachments/assets/50711193-c894-41be-a459-7cdb861823b4" />

## Switchs
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/ef9147da-41e1-4a97-b20f-3bde2ce49006" />

## Keycaps
<img width="1200" height="334" alt="image" src="https://github.com/user-attachments/assets/a640b9dc-0331-47e3-b517-b4cddaf3dc42" />

## USB-c Cable
<img width="1200" height="1199" alt="image" src="https://github.com/user-attachments/assets/f09141ba-24b1-4c49-b03f-cbbbab19a6b7" />



# BOM

| Quantity      | Parts         | Description   | Suppliers     | Price         |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 1x  | RaspberryPi Pico  | This will be the main part of the keyboard—the component that actually makes it function and respond to all of the user's commands.  | [RaspberryPi Pico](https://www.google.com/aclk?sa=L&ai=DChsSEwibxe-8_9eXAxX4VUgAHYpNKHsYACICCAEQChoCY2U&co=1&ase=2&gclid=CjwKCAjw9PvWBhAxEiwAddzYyYSJZ7UXpklbmFzkP8O3EFmvRU4AtTAiUxpHr_9tkhAvw0_RXMD6dxoCH_UQAvD_BwE&cid=CAAS9QHkaBhD6FbWmHBN7MsDVew-0O9MhhjhIk7VtOfQ49BJhjWOsTSFw6bp9yYYFJ5JKXmd-5HlOupdWXErJn4rQBD4zEQBMx2k93VtfnZNmJsqhQl4dindNntgzA1MGSygfU4WBlBbf2g3GR71w-paDlBHAieKfWmn8Q8aF84Z_ALl27jHaUSn44IKSyyzx1Ctnc0VlIKf7s117n3O0QQEuqRqYpVqkuyavaDcBinwQSb-BUZyAK75_QBhayI-lT0iP4xrCdrz7IJu-AcpH4WNwdGSV32M8N-7CmS_lCGfJiR7hDXAUFte0_lgmTn8vMXgSMeHjBBceA&cce=2&category=acrcp_v1_32&sig=AOD64_3wK0zsBjN2-6bpFfc1b0CkzevsDA&ctype=5&q=&nis=4&ved=2ahUKEwjZgei8_9eXAxWoHrkGHQ5hHygQ5bgDKAB6BAgOEAs&adurl=) | $6.2  |
| 87x | Diode 1N4148  | The diode serves to prevent double-clicking and the ghosting effect on the keyboard. | [Diode 1N4148](https://www.mercadolivre.com.br/kit-10-diodos-retificadores-1n4148-1000v-02a-stg-eletro-vidro-passivado/p/MLB27103607?pdp_filters=item_id%3AMLB3798508313&from=gshop&matt_tool=56164162&matt_word=&matt_source=google&matt_campaign_id=22090193744&matt_ad_group_id=194474654154&matt_match_type=&matt_network=g&matt_device=c&matt_creative=792355615410&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735098660&matt_product_id=MLB27103607-product&matt_product_partition_id=2495059736147&matt_target_id=aud-1967662333334:pla-2495059736147&cq_src=google_ads&cq_cmp=22090193744&cq_net=g&cq_plt=gp&cq_med=pla&gad_source=1&gad_campaignid=22090193744&gbraid=0AAAAAD93qcAFXS1D6HAsi0Wi-mlFE3ZrU&gclid=CjwKCAjw9PvWBhAxEiwAddzYydhtHdCHVoedVGiZSYBDaSSydb0Fx_Z1XWSCBVeinyjqGIG87Sv_yRoC2DcQAvD_BwE)  |  $8  |
| 4x | Stabilizers | As the name itself suggests, this is a stabilizer. Since some parts are larger, this is used to keep them from wobbling. | [Stabilizers](https://pt.aliexpress.com/item/1005011961905061.html?spm=a2g0o.productlist.main.2.77404c8agv3Zpj&algo_pvid=c416a962-3552-4e1e-b0d2-356b99ff4161&algo_exp_id=c416a962-3552-4e1e-b0d2-356b99ff4161-1&pdp_ext_f=%7B%22order%22%3A%2261%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21BRL%2138.51%2138.51%21%21%2147.64%2147.64%21%402101c69517930290229327326e0f42%2112000057150856776%21sea%21BR%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A4e7cc88e%3Bm03_new_user%3A-29895&curPageLogUid=fAcMEu0ju6qA&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005011961905061%7C_p_origin_prod%3A) | $10.5  |
| 88x | Switchs  | This component is what allows commands to be sent to the controller, indicating which key the user wants to press. | [Switchs](https://www.mercadolivre.com.br/kit-10-clicker-teclado-mecanico-azul-3-pinos-switch-gamer/up/MLBU4799799250?pdp_filters=item_id%3AMLB7442852240&from=gshop&matt_tool=31485049&matt_word=&matt_source=google&matt_campaign_id=22090354244&matt_ad_group_id=191786791161&matt_match_type=&matt_network=g&matt_device=c&matt_creative=782869963634&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=5756723143&matt_product_id=MLBU4799799250&matt_product_partition_id=2498613880064&matt_target_id=aud-1967662333334:pla-2498613880064&cq_src=google_ads&cq_cmp=22090354244&cq_net=g&cq_plt=gp&cq_med=pla&gad_source=1&gad_campaignid=22090354244&gbraid=0AAAAAD93qcCIKBSjcXEdc9_dg7ThbMKog&gclid=CjwKCAjw9PvWBhAxEiwAddzYyTBkgcE5iz3weebgTrAdZ9NQqK1G1vc-NDPvYyXmfEVYPgfHyPvkehoC4xEQAvD_BwE) |  $34  |
| 88x | Keycaps  | This is basically the part you’ll be able to click on; without it, you’d just have a bunch of random pins that don’t make any sense lol | [Keycaps](https://www.mercadolivre.com.br/kit-de-keycaps-redragon-degrade-verde-abnt2-106-teclas-abs/p/MLB54150952?pdp_filters=item_id%3AMLB4289903217&from=gshop&matt_tool=83591963&matt_word=&matt_source=google&matt_campaign_id=22090193903&matt_ad_group_id=194474632074&matt_match_type=&matt_network=g&matt_device=c&matt_creative=792355616043&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735128761&matt_product_id=MLB54150952-product&matt_product_partition_id=2496085499453&matt_target_id=aud-1967662333334:pla-2496085499453&cq_src=google_ads&cq_cmp=22090193903&cq_net=g&cq_plt=gp&cq_med=pla&gad_source=1&gad_campaignid=22090193903&gbraid=0AAAAAD93qcCRuFOxaXQNEiNnHxQu-nWmm&gclid=CjwKCAjw9PvWBhAxEiwAddzYyQF_TCt68xujzzVDeMJ7RKth2i88PenlMMTJps7kogIt2-d3XBUaTBoCNakQAvD_BwE) |  $16  |
| 1x | USB-C cable  | Without this, the keyboard won't work, as it won't receive any charge. | [USB-C Cable](https://produto.mercadolivre.com.br/MLB-6128401728-cabo-coiled-teclado-mecnico-usb-tipo-c-conector-aviador-_JM?matt_tool=56164162&matt_word=&matt_source=google&matt_campaign_id=22090193744&matt_ad_group_id=194474654154&matt_match_type=&matt_network=g&matt_device=c&matt_creative=792355615410&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=296849702&matt_product_id=MLB6128401728&matt_product_partition_id=2495059736307&matt_target_id=aud-1967662333334:pla-2495059736307&cq_src=google_ads&cq_cmp=22090193744&cq_net=g&cq_plt=gp&cq_med=pla&gad_source=1&gad_campaignid=22090193744&gbraid=0AAAAAD93qcAFXS1D6HAsi0Wi-mlFE3ZrU&gclid=CjwKCAjw9PvWBhAxEiwAddzYyeyiGedMsmeVZ_o-1LvWcwa25IfkgyL4xbatIPCuwWQzTEjeJqRTXBoCOCsQAvD_BwE) | $13.46 |
| total cost:     | - |  Some are all-inclusive—shipping and everything—but others aren't. You only find out once you add everything to your cart.| - | 88,16|

