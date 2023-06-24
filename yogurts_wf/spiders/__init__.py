import json
import scrapy


class YogurtsSpider(scrapy.Spider):
    name = "yogurts"

    def start_requests(self):
        urls = ['https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-plain-grassfed-greek-yogurt-15-lb-b0785wcqbf',
            'https://www.wholefoodsmarket.com/product/chobani-plain-greek-yogurt-32-oz-b008u5ostq',
            'https://www.wholefoodsmarket.com/product/chobani-greek-yogurt-vanilla-blended-32-oz-b00cj8mjg4',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-greek-yogurt-plain-32-oz-b07myg86vs',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-greek-nonfat-plain-yogurt-32-oz-b07myd18hm',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-365-everyday-value-organic-plain-whole-milk-yogurt-32-oz-b074h7kkrv',
            'https://www.wholefoodsmarket.com/product/wallaby-organic-whole-milk-greek-yogurt-blended-vanilla-bean-32-oz-b00lmaxcoi',
            'https://www.wholefoodsmarket.com/product/wallaby-yogurt-greek-plain-organic-32-oz-b00k1xkuym',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-plain-whole-milk-yogurt-2-lb-b00108epcu',
            'https://www.wholefoodsmarket.com/product/fage-total-0-plain-greek-yogurt-53-oz-b000vtwd64',
            'https://www.wholefoodsmarket.com/product/siggis-4-plain-skyr-yogurt-24-oz-b01knz4qec',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-icelandic-skyr-nonfat-yogurt-plain-24-oz-b00lmc4xvw',
            'https://www.wholefoodsmarket.com/product/redwood-hill-farm-plain-goat-milk-yogurt-32-oz-b000qjfmnu',
            'https://www.wholefoodsmarket.com/product/fage-total-0-plain-greek-yogurt-16-oz-b000vrc1ng',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-icelandic-skyr-nonfat-yogurt-vanilla-24-oz-b00lmc502s',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-0-fat-plain-greek-yogurt-2-lb-b00b03xdpa',
            'https://www.wholefoodsmarket.com/product/straus-family-creamery-organic-plain-greek-yogurt-32-oz-b00naj0jk4',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-lowfat-yogurt-smoothies-strawberry-banana-6-ct-116-pt-b00cfy665w',
            'https://www.wholefoodsmarket.com/product/chobani-0-greek-yogurt-with-strawberry-on-the-bottom-53-oz-b002gvjzi4',
            'https://www.wholefoodsmarket.com/product/so-delicious-dairy-free-dairy-free-coconut-milk-yogurt-alternative-unsweetened-vanilla-vegan-nongmo-project-verified-24-oz-b07895lgcc',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-plain-yogurt-low-fat-32-oz-b074h64byn',
            'https://www.wholefoodsmarket.com/product/fage-total-2-greek-yogurt-16-oz-b004ibvvc8',
            'https://www.wholefoodsmarket.com/product/chobani-0-greek-yogurt-blended-with-vanilla-53-oz-b002gvjz4i',
            'https://www.wholefoodsmarket.com/product/bellwether-farms-plain-sheep-milk-yogurt-24-oz-b08ngc4nm5',
            'https://www.wholefoodsmarket.com/product/wallaby-yogurt-greek-plain-low-fat-organic-32-oz-b00k1xkuo2',
            'https://www.wholefoodsmarket.com/product/brown-cow-plain-cream-top-yogurt-2-lb-b000o6k8m0',
            'https://www.wholefoodsmarket.com/product/maple-hill-creamery-organic-plain-kefir-32-oz-b071y2xfp2',
            'https://www.wholefoodsmarket.com/product/chobani-0-greek-yogurt-with-peach-on-the-bottom-53-oz-b002gvk07o',
            'https://www.wholefoodsmarket.com/product/lifeway-kefir-cultured-whole-milk-141-fl-oz-b07dfwt423',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-yokids-blueberry-strawberry-vanilla-lowfat-yogurt-4-oz-b00108hzao',
            'https://www.wholefoodsmarket.com/product/siggis-0-vanilla-skyr-yogurt-53-oz-b002m3zbpw',
            'https://www.wholefoodsmarket.com/product/maple-hill-creamery-plain-cream-on-top-yogurt-32-oz-b071ybl28j',
            'https://www.wholefoodsmarket.com/product/wallaby-organic-aussie-greek-plain-nonfat-yogurt-32-oz-b00dihm32u',
            'https://www.wholefoodsmarket.com/product/fage-total-plain-greek-yogurt-53-oz-b000wob94u',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-whole-milk-strawberry-beet-berry-yogurt-pouch-35-oz-b00myuqb52',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-blueberry-whole-milk-yogurt-pouch-35-oz-b00myuqask',
            'https://www.wholefoodsmarket.com/product/siggis-strawberry-banana-kids-yogurt-pouches-35-oz-b0837hkffm',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-low-fat-strawberry-yogurt-pouch-35-oz-b00myuqb3o',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-yogurt-whole-milk-vanilla-32-oz-b07dwfvnzb',
            'https://www.wholefoodsmarket.com/product/fage-total-2-honey-greek-yogurt-53-oz-b0012zgi26',
            'https://www.wholefoodsmarket.com/product/chobani-0-greek-yogurt-with-blueberry-on-the-bottom-53-oz-b002gvjzs4',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-strawberry-smoothie-6-fl-oz-b00108epuc',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-yogurt-lowfat-vanilla-32-oz-b074h5y3tm',
            'https://www.wholefoodsmarket.com/product/fage-total-2-peach-greek-yogurt-53-oz-b0012zcpm8',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-plain-whole-milk-greek-yogurt-19-lb-b01nbbvpli',
            'https://www.wholefoodsmarket.com/product/noosa-vanilla-yoghurt-4-pk-16-oz-b01c6va7qw',
            'https://www.wholefoodsmarket.com/product/noosa-lemon-yoghurt-8-oz-b004kz0vx2',
            'https://www.wholefoodsmarket.com/product/fage-total-2-black-cherry-greek-yogurt-53-oz-b0012zi8a6',
            'https://www.wholefoodsmarket.com/product/chobani-0-greek-yogurt-with-black-cherry-on-the-bottom-53-oz-b008u5oq0m',
            'https://www.wholefoodsmarket.com/product/straus-family-creamery-whole-milk-yogurt-plain-32-oz-b000o6gaue',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-icelandic-skyr-nonfat-yogurt-acai-mixed-berry-53-oz-b002m3zbno',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-french-vanilla-whole-milk-yogurt-2-lb-b00108hzfy',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-icelandic-skyr-whole-milk-yogurt-touch-of-honey-24-oz-b07811xcgj',
            'https://www.wholefoodsmarket.com/product/siggis-4-vanilla-skyr-yogurt-44-oz-b011yjq4b4',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-kids-strawberry-banana-lowfat-yogurt-tubes-2-oz-each-8-ct-b072ztr9pl',
            'https://www.wholefoodsmarket.com/product/chobani-less-sugar-madagascar-vanilla-cinnamon-greek-yogurt-53-oz-b07cn8y436',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-icelandic-skyr-nonfat-yogurt-peach-53-oz-b00cijm0po',
            'https://www.wholefoodsmarket.com/product/siggis-mixed-berries-53oz-plant-based-coconut-blend-b07yqgk9tw',
            'https://www.wholefoodsmarket.com/product/la-fermiere-vanilla-bean-french-yogurt-49-oz-b07fyh7w7n',
            'https://www.wholefoodsmarket.com/product/siggis-4-mixed-berries-skyr-yogurt-44-oz-b011yjqbrg',
            'https://www.wholefoodsmarket.com/product/chobani-monterey-strawberry-less-sugar-greek-yogurt-53-oz-b07cn36j65',
            'https://www.wholefoodsmarket.com/product/chobani-0-greek-yogurt-with-raspberry-on-the-bottom-53-oz-b006jvikl0',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-lowfat-plain-yogurt-2-lb-b000qjdyty',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-icelandic-skyr-nonfat-yogurt-strawberry-53-oz-b00cijlxz2',
            'https://www.wholefoodsmarket.com/product/white-mountain-organic-whole-milk-bulgarian-yogurt-32-fl-oz-b015hvymau',
            'https://www.wholefoodsmarket.com/product/icelandic-provisions-peach-cloudberry-skyr-53-oz-b01gv64r0k',
            'https://www.wholefoodsmarket.com/product/la-fermiere-orange-blossom-honey-french-yogurt-49-oz-b07fydlwq8',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-blueberry-yogurt-pouches-35-oz-b075lyr6y4',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-plantbased-coconut-blend-vanilla-24-oz-tub-b08ngdkspw',
            'https://www.wholefoodsmarket.com/product/noosa-vanilla-yogurt-24-oz-b079nfkn7t',
            'https://www.wholefoodsmarket.com/product/noosa-blueberry-yoghurt-8-oz-b00cijm61w',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-yobaby-blueberry-apple-yogurt-6pk-4-oz-b01hxz03si',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-strawberry-whole-milk-probiotic-yogurt-2-lb-b00108grty',
            'https://www.wholefoodsmarket.com/product/icelandic-provisions-key-lime-skyr-53-oz-b0727lgc9s',
            'https://www.wholefoodsmarket.com/product/icelandic-provisions-coconut-skyr-53-oz-b01gv64qe2',
            'https://www.wholefoodsmarket.com/product/la-fermiere-pressed-lemon-french-yogurt-49-oz-b07fyztp6t',
            'https://www.wholefoodsmarket.com/product/brown-cow-maple-cream-top-yogurt-2-lb-b000o6efyw',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-low-fat-vanilla-yogurt-2-lb-b00108cspq',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-kefir-plain-32-fl-oz-b07n1pw3wn',
            'https://www.wholefoodsmarket.com/product/biok-plus-strawberry-dairy-probiotic-21-fl-oz-b017kqzrwm',
            'https://www.wholefoodsmarket.com/product/noosa-blueberry-yoghurt-4-pk-b004kz45dy',
            'https://www.wholefoodsmarket.com/product/culina-coconut-yogurt-blueberry-lavender-5-oz-b07n1pjczn',
            'https://www.wholefoodsmarket.com/product/siggis-triple-cream-vanilla-yogurt-4-oz-b07437zlxn',
            'https://www.wholefoodsmarket.com/product/siggis-0-blueberry-skyr-yogurt-53-oz-b002m3zbhu',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-2-icelandic-skyr-lowfat-yogurt-key-lime-53-oz-b0844xrkk8',
            'https://www.wholefoodsmarket.com/product/so-delicious-dairy-free-coconut-milk-yogurt-alternative-peach-vegan-nongmo-project-verified-53-oz-b072xmndvf',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-2-icelandic-skyr-lowfat-yogurt-black-cherry-53-oz-b01knz4qbk',
            'https://www.wholefoodsmarket.com/product/noosa-raspberry-yoghurt-8-oz-b00cj5r9ia',
            'https://www.wholefoodsmarket.com/product/brown-cow-vanilla-cream-top-yogurt-53-oz-b000o6gam2',
            'https://www.wholefoodsmarket.com/product/wallaby-organic-aussie-greek-whole-milk-yogurt-strawberry-32-oz-usda-organic-b0785wfkrz',
            'https://www.wholefoodsmarket.com/product/green-valley-creamery-lactose-free-whole-milk-plain-yogurt-24-oz-b07fw8qn5b',
            'https://www.wholefoodsmarket.com/product/siggis-strawberry-yogurt-4-pack-53-oz-b08v8cjmlz',
            'https://www.wholefoodsmarket.com/product/noosa-strawberry-rhubarb-yoghurt-8-oz-b00cijmarw',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-yogurt-whole-milk-strawberry-6-4-ounce-cups-24-oz-b07dwg98cm',
            'https://www.wholefoodsmarket.com/product/ellenos-real-greek-yogurt-passionfruit-53-oz-b07txdvzpj',
            'https://www.wholefoodsmarket.com/product/noosa-vanilla-bean-yoghurt-8-oz-b07fybydhg',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-vanilla-grass-fed-greek-yogurt-15-lb-b08ngcvkmk',
            'https://www.wholefoodsmarket.com/product/brown-cow-maple-whole-milk-yogurt-53-oz-b07kfhcydh',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-plantbased-coconut-blend-peach-53-oz-b08ng9h4wy',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-organic-vanilla-whole-milk-yogurt-35-oz-b00myuq5ps',
            'https://www.wholefoodsmarket.com/product/siggis-raspberry-53oz-plant-based-coconut-blend-b07yqgbjs5',
            'https://www.wholefoodsmarket.com/product/biok-plus-strawberry-fermented-dairy-probiotic-12-pk-42-fl-oz-b014jvphiu',
            'https://www.wholefoodsmarket.com/product/so-delicious-dairy-free-coconut-milk-yogurt-alternative-strawberry-banana-vegan-nongmo-project-verified-53-oz-b071h7rzmb',
            'https://www.wholefoodsmarket.com/product/brown-cow-cherry-vanilla-cream-top-yogurt-6-oz-53-oz-b000o6gapy',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-probiotic-drinkable-whole-milk-yogurt-strawberry-8-oz-b06xrr9dzt',
            'https://www.wholefoodsmarket.com/product/chobani-flip-smore-smores-greek-yogurt-45-oz-b01m5k1apr',
            'https://www.wholefoodsmarket.com/product/noosa-coconut-yoghurt-8-oz-b004kyxqzs',
            'https://www.wholefoodsmarket.com/product/biok-plus-blueberry-fermented-rice-probiotic-12pl-42-fl-oz-b01esbnqxo',
            'https://www.wholefoodsmarket.com/product/siggis-vanilla-yogurt-4-count-53-oz-b08v7pvdmp',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-plantbased-coconut-blend-toasted-coconut-53oz-b08ngcn3p8',
            'https://www.wholefoodsmarket.com/product/noosa-honey-yoghurt-8-oz-b00cj5rc8m',
            'https://www.wholefoodsmarket.com/product/so-delicious-dairy-free-dairy-free-coconut-milk-yogurt-alternative-key-lime-vegan-nongmo-project-verified-53-oz-b072xnv11r',
            'https://www.wholefoodsmarket.com/product/ellenos-greek-yogurt-lemon-curd-53-oz-b07schcb3t',
            'https://www.wholefoodsmarket.com/product/culina-sour-cherry-almond-coconut-yogurt-5-oz-b08gz7ptyj',
            'https://www.wholefoodsmarket.com/product/green-valley-creamery-lactose-free-low-fat-plain-kefir-32-fl-oz-b085m81n37',
            'https://www.wholefoodsmarket.com/product/siggis-raspberry-nonfat-drinkable-yogurt-32-fl-oz-b00lmc4xlc',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-kefir-strawberry-32-fl-oz-b07n1n38pq',
            'https://www.wholefoodsmarket.com/product/green-valley-creamery-lactose-free-whole-milk-plain-kefir-32-fl-oz-b085m87hzt',
            'https://www.wholefoodsmarket.com/product/siggis-0-plain-filmjolk-drinkable-yogurt-32-fl-oz-b00lmc4tuw',
            'https://www.wholefoodsmarket.com/product/redwood-hill-farm-plain-goat-milk-yogurt-6-oz-b000yn1e5i',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-probiotic-peach-lowfat-yogurt-protein-smoothie-10-fl-oz-b00108ct1y',
            'https://www.wholefoodsmarket.com/product/ellenos-mango-greek-yogurt-53-oz-b07s98hh62',
            'https://www.wholefoodsmarket.com/product/nancys-yogurt-plain-whole-milk-yogurt-tub-32-oz-b000vhwlhw',
            'https://www.wholefoodsmarket.com/product/so-delicious-dairy-free-coconut-milk-yogurt-alternative-chocolate-vegan-nongmo-project-verified-53-oz-b078837c7l',
            'https://www.wholefoodsmarket.com/product/chobani-flip-almond-coco-loco-greek-yogurt-45-oz-b00cj8mda6',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-probiotic-drinkable-whole-milk-yogurt-blueberry-8-oz-b06xsg4s4g',
            'https://www.wholefoodsmarket.com/product/ellenos-real-greek-yogurt-marionberry-53-oz-b07sdkwmzd',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-strawberry-probiotic-lowfat-yogurt-protein-smoothie-10-fl-oz-b0051g7ets',
            'https://www.wholefoodsmarket.com/product/siggis-vanilla-whole-milk-yogurt-drink-8-fl-oz-b06xsc89wz',
            'https://www.wholefoodsmarket.com/product/365-everyday-value-vanilla-organic-yogurt-53-ounce-b07dwsd915',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-yogurt-whole-milk-blueberry-6-4-ounce-cups-24-oz-b07dwfrhzr',
            'https://www.wholefoodsmarket.com/product/straus-family-creamery-organic-plain-nonfat-greek-yogurt-32-oz-b0147qh6ke',
            'https://www.wholefoodsmarket.com/product/kite-hill-artisan-almond-milk-strawberry-yogurt-53-ounce-b06vv87wdj',
            'https://www.wholefoodsmarket.com/product/fage-total-2-strawberry-greek-yogurt-53-oz-b0012zedtg',
            'https://www.wholefoodsmarket.com/product/siggis-0-vanilla-filmjolk-drinkable-yogurt-32-fl-oz-b00lmc4xiu',
            'https://www.wholefoodsmarket.com/product/siggis-mixed-berry-non-fat-yogurt-4-pack-53-oz-b097cn2rwk',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-raspberry-kefir-32-fl-oz-b07n1nz3pf',
            'https://www.wholefoodsmarket.com/product/alexandre-family-farms-organic-plain-yogurt-24-oz-b09kpdtwrr',
            'https://www.wholefoodsmarket.com/product/pillars-mixed-berry-greek-drinkabe-yogurt-32-fl-oz-b08qfqbxrh',
            'https://www.wholefoodsmarket.com/product/wallaby-organic-aussie-greek-yogurt-no-sugar-added-strawberry-53-oz-usda-organic-b07qbdc1kn',
            'https://www.wholefoodsmarket.com/product/maple-hill-creamery-organic-vanilla-whole-milk-yogurt-32-oz-b078fbc723',
            'https://www.wholefoodsmarket.com/product/wallaby-organic-aussie-smooth-whole-milk-yogurt-vanilla-32-oz-usda-organic-b0010xt5gg',
            'https://www.wholefoodsmarket.com/product/siggis-vanilla-non-fat-skyr-yogurt-4-pack-53-oz-b097cmq51p',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-yogurt-whole-milk-strawberry-53-oz-b07dwg8vp2',
            'https://www.wholefoodsmarket.com/product/biok-plus-original-fermented-dairy-probiotic-12-pk-42-fl-oz-b01esbni3m',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-kefir-blueberry-32-fl-oz-b07n1pb63r',
            'https://www.wholefoodsmarket.com/product/bellwether-farms-plain-sheep-milk-yogurt-6-oz-b00n42bjf6',
            'https://www.wholefoodsmarket.com/product/pillars-drinkable-greek-yogurt-mixed-berry-12-fl-oz-b07d6tzy4m',
            'https://www.wholefoodsmarket.com/product/straus-family-creamery-nonfat-yogurt-plain-32-oz-b000o6gauy',
            'https://www.wholefoodsmarket.com/product/kite-hill-artisan-almond-milk-blueberry-yogurt-53-oz-b06w551btg',
            'https://www.wholefoodsmarket.com/product/brown-cow-strawberry-whole-milk-yogurt-53-oz-b000o6ice6',
            'https://www.wholefoodsmarket.com/product/fage-blended-vanilla-yogurt-32-oz-b0932zt2bv',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-whole-milk-vanilla-kefir-32-fl-oz-b08rb2p2cx',
            'https://www.wholefoodsmarket.com/product/pillars-drinkable-greek-yogurt-strwbrry-banana-12-fl-oz-b07d6v4nfw',
            'https://www.wholefoodsmarket.com/product/fage-total-2-blueberry-greek-yogurt-53-oz-b003yv04yo',
            'https://www.wholefoodsmarket.com/product/pillars-peach-drinkable-greek-yogurt-12-fl-oz-b084tp88q1',
            'https://www.wholefoodsmarket.com/product/nancys-yogurt-organic-plain-lowfat-yogurt-32-oz-b000vhymn8',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-organic-yogurt-whole-milk-blueberry-53-oz-b07dwgfq1r',
            'https://www.wholefoodsmarket.com/product/gogo-squeez-yogurtz-strawberry-12-oz-b01gsaeyqg',
            'https://www.wholefoodsmarket.com/product/bellwether-farms-blackberry-sheep-milk-yogurt-6-oz-b0147qlveq',
            'https://www.wholefoodsmarket.com/product/harmless-harvest-unsweetened-coconut-yogurt-drink-24-fl-oz-b081dkvrw7',
            'https://www.wholefoodsmarket.com/product/clio-snacks-strawberry-greek-yogurt-bar-1-each-b078fhcjfz',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-strawberry-banana-yogurt-pouches-35-oz-b0716bftl2',
            'https://www.wholefoodsmarket.com/product/wallaby-organic-aussie-greek-yogurt-no-sugar-added-vanilla-chai-53-oz-usda-organic-b07qffxmzx',
            'https://www.wholefoodsmarket.com/product/the-coconut-cult-chocolate-mousse-coconut-yogurt-8-fl-oz-b07xc8fcz2',
            'https://www.wholefoodsmarket.com/product/pillars-chocolate-drinkable-greek-yogurt-32-fl-oz-2g2u8pso',
            'https://www.wholefoodsmarket.com/product/pillars-chocolate-drinkable-greek-yogurt-32-fl-oz-b0954hy7p8',
            'https://www.wholefoodsmarket.com/product/culina-plain-simple-alternative-yogurt-16-oz-b081w446kz',
            'https://www.wholefoodsmarket.com/product/gogo-squeez-yogurtz-banana-12-oz-b01gsaez5g',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-greek-yogurt-plain-nonfat-32-oz-b07cwc1z79',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-traditional-plain-kefir-32-fl-oz-b015hvxt3q',
            'https://www.wholefoodsmarket.com/product/straus-family-creamery-european-style-organic-plain-whole-milk-yogurt-16-oz-b07d8f6gms',
            'https://www.wholefoodsmarket.com/product/saint-benoit-creamery-organic-plain-french-style-yogurt-475-oz-b0785wfksw',
            'https://www.wholefoodsmarket.com/product/pavels-original-plain-whole-milk-yogurt-32-oz-b0010wgsvc',
            'https://www.wholefoodsmarket.com/product/yasso-frozen-greek-yogurt-coffee-chocolate-chip-frozen-greek-yogurt-bars-14-fl-oz-b010owezuy',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-summer-strawberry-kefir-32-fl-oz-b074hz2yc1',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-lowfat-peach-yogurt-6-oz-b07pqnj6wf',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-strawberry-cream-on-top-yogurt-6-oz-b019p8vk1k',
            'https://www.wholefoodsmarket.com/product/saint-benoit-creamery-organic-strawberry-french-style-yogurt-475-oz-b015hw0dcu',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-nondairy-almondmilk-yogurt-mango-53-oz-b07rc8bsct',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-lowfat-strawberry-yogurt-6-oz-b079nptk5z',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-low-fat-blueberry-yogurt-6-oz-b079n3svxb',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-peach-cream-on-top-yogurt-6-oz-b019p8vkr4',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-lowfat-vanilla-bean-yogurt-6-oz-b079nmf8q6',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-plain-low-fat-yogurt-32-oz-b079n54k7m',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-low-fat-vanilla-bean-yogurt-32-oz-b079nn8fdr',
            'https://www.wholefoodsmarket.com/product/pavels-yogurt-organic-low-fat-russian-yogurt-24-oz-b07prwg2gm',
            'https://www.wholefoodsmarket.com/product/clover-sonoma-blueberry-whole-milk-yogurt-6-oz-b019p8vld2',
            'https://www.wholefoodsmarket.com/product/forest-berry-yogurt-6-oz-b019p8vj20',
            'https://www.wholefoodsmarket.com/product/dosa-cayenne-tamarind-lassi-8-fl-oz-b07fykdt15',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-whole-milk-mixed-berry-kefir-32-fl-oz-b01df1o088',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-nondairy-almondmilk-yogurt-strawberry-53-oz-b07rcngxj9',
            'https://www.wholefoodsmarket.com/product/365-by-whole-foods-market-nondairy-almondmilk-yogurt-vanilla-53-oz-b07rcn9m14',
            'https://www.wholefoodsmarket.com/product/culina-coconut-yogurt-5-oz-2fj8qlak',
            'https://www.wholefoodsmarket.com/product/fage-2-milkfat-greek-yogurt-53-oz-b000vr81ia',
            'https://www.wholefoodsmarket.com/product/chobani-strawberry-yogurt-4-pack-212-oz-b00m8zejuw',
            'https://www.wholefoodsmarket.com/product/chobani-peach-yogurt-4-pack-212-oz-b00xuy1lre',
            'https://www.wholefoodsmarket.com/product/chobani-vanilla-mixed-berry-greek-yogurt-4-pack-53-oz-b07jzx58vm',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-low-fat-strawberry-kefir-4pk-14-fl-oz-b08rb2nm1h',
            'https://www.wholefoodsmarket.com/product/chobani-mixed-berry-vanilla-green-yogurt-10-fl-oz-b08bjyxx16',
            'https://www.wholefoodsmarket.com/product/chobani-strawberry-cream-greek-yogurt-drink-10-fl-oz-b08bjw9tnz',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-icelandic-skyr-nonfat-yogurt-plain-53-oz-b002m3zbei',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-2-icelandic-skyr-lowfat-yogurt-coconut-53-oz-b00lm1928c',
            'https://www.wholefoodsmarket.com/product/alexandre-family-farms-organic-plain-grassfed-low-fat-a2-yogurt-24-oz-b0bdgncc49',
            'https://www.wholefoodsmarket.com/product/alexandre-family-farms-organic-a2a2-grass-fed-whole-milk-kefir-28-fl-oz-b0bfmtjjrb',
            'https://www.wholefoodsmarket.com/product/alexandre-family-farms-organic-a2a2-grass-fed-lowfat-kefir-28-fl-oz-b0bfmpnd7m',
            'https://www.wholefoodsmarket.com/product/fage-total-plain-5-16-oz-b000wo9ore',
            'https://www.wholefoodsmarket.com/product/yasso-frozen-greek-yogurt-mint-chocolate-chip-frozen-greek-yogurt-4-pk-14-fl-oz-b01gvg81ca',
            'https://www.wholefoodsmarket.com/product/fage-plain-lactose-free-yogurt-32-oz-b09335srxf',
            'https://www.wholefoodsmarket.com/product/dosa-peppercorn-berry-lassi-8-fl-oz-b07c774rpk',
            'https://www.wholefoodsmarket.com/product/dosa-turmeric-banana-lassi-8-fl-oz-b07c7424dk',
            'https://www.wholefoodsmarket.com/product/bellwether-farms-vanilla-sheep-milk-yogurt-6-oz-b00n42bke6',
            'https://www.wholefoodsmarket.com/product/dosa-cardamom-mango-lassi-8-fl-oz-b07c78s674',
            'https://www.wholefoodsmarket.com/product/siggis-siggis-lemon-skyr-icelandicstyle-strained-triple-cream-yogurt-4-oz-b074395wqw',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-low-fat-mixed-berry-kefir-4pk-14-fl-oz-b0954hph5y',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-strawberry-berry-and-beet-yogurt-35-oz-b00rqjcuhy',
            'https://www.wholefoodsmarket.com/product/icelandic-provisions-extra-creamy-lemon-44-oz-b08qlzb6s3',
            'https://www.wholefoodsmarket.com/product/noosa-coconut-almond-chocolate-yoghurt-mates-58-oz-b0bbphy5fk',
            'https://www.wholefoodsmarket.com/product/icelandic-provisions-plain-whole-milk-skyr-yogurt-30-oz-b0b2v1fght',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-whole-milk-mango-kefir-32-fl-oz-b08r9yq573',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-kids-pear-spinach-mango-whole-milk-yogurt-pouch-35-oz-b072ztygd6',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-coconut-honey-whole-milk-kefir-32-fl-oz-b087nl33rl',
            'https://www.wholefoodsmarket.com/product/icelandic-provisions-plain-lowfat-skyr-yogurt-30-oz-b0b2vj56bq',
            'https://www.wholefoodsmarket.com/product/noosa-peach-yoghurt-8-oz-b00lmc47ea',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-whole-milk-plain-kefir-32-fl-oz-b013jl49pi',
            'https://www.wholefoodsmarket.com/product/stonyfield-organic-organic-wild-berry-smoothie-6-fl-oz-b00108grps',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-kefir-strawnana-probugs-35-fl-oz-b07dfx4f5c',
            'https://www.wholefoodsmarket.com/product/fage-total-plain-5-32-oz-b00wtr0cdm',
            'https://www.wholefoodsmarket.com/product/fage-total-plain-2-32-oz-b00fzheggw',
            'https://www.wholefoodsmarket.com/product/lifeway-organic-lowfat-plain-kefir-32-fl-oz-b000qjc5ki',
            'https://www.wholefoodsmarket.com/product/fage-total-plain-0-32-oz-b006wbvsv6',
            'https://www.wholefoodsmarket.com/product/horizon-organic-low-fat-yogurt-strawberry-453-oz-b08m7ctf9q',
            'https://www.wholefoodsmarket.com/product/redwood-hill-farm-traditional-plain-kefir-32-fl-oz-b00fzhepmw',
            'https://www.wholefoodsmarket.com/product/petit-pot-strawberry-cheesecake-dessert-cup-2-pack-7-oz-b0bhmwqfgr'
            ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        s = response.xpath('//script/text()').extract()
        d = json.loads(s[-1])

        yield { 'link': response.request.url,
                'name': d['props']['pageProps']['data']['name'],
                'brand': d['props']['pageProps']['data']['brand']['name'],
                'diets': d['props']['pageProps']['data']['diets'],
                'categories': d['props']['pageProps']['data']['categories'],
                'images': d['props']['pageProps']['data']['images'],
                'ingredients': d['props']['pageProps']['data']['ingredients'],
                'nutritionElements': d['props']['pageProps']['data']['nutritionElements'],
                'servingInfo': d['props']['pageProps']['data']['servingInfo'] }

    # execute with: scrapy crawl yogurts -o wf-yog.jsonl
