import pickle

train_list = [3410, 3870, 8528, 8573, 8723, 4972, 2482, 5354, 634, 6764, 1337, 2700, 9835, 1883, 649, 6762, 3194, 6076, 4815, 7813, 94, 7773, 1163, 6294, 9239, 1137, 4376, 2469, 4392, 5308, 4223, 5165, 225, 3516, 9650, 5147, 1477, 1619, 768, 167, 6, 5545, 1886, 8336, 3822, 6020, 443, 5767, 7488, 2821, 7723, 446, 4957, 1955, 1869, 5734, 1652, 1594, 7902, 3053, 6622, 4298, 7411, 9477, 2852, 7950, 55, 295, 8703, 2047, 5647, 2199, 1101, 6661, 6978, 7590, 847, 7961, 1386, 4508, 321, 1033, 1729, 8778, 4468, 1450, 9766, 2020, 9402, 5192, 7802, 7734, 286, 4161, 1482, 2578, 9253, 3500, 6831, 224, 4215, 4521, 6298, 8135, 2642, 6621, 2937, 8068, 2455, 3546, 8310, 2171, 6199, 7563, 8361, 1019, 8912, 8808, 7354, 568, 7938, 9192, 2237, 349, 8277, 2300, 8873, 21, 7524, 4162, 9538, 5500, 4385, 2891, 8825, 8313, 4424, 3374, 440, 1157, 9277, 9873, 1882, 4742, 4945, 1480, 8040, 476, 4412, 5087, 4636, 6727, 9340, 1847, 5719, 3587, 3117, 1645, 4069, 2032, 8445, 3102, 8143, 6078, 1378, 2345, 2385, 5871, 438, 3736, 6047, 1701, 2111, 8779, 7819, 4489, 9757, 5076, 1227, 3893, 3382, 1208, 1098, 835, 279, 6664, 5151, 4620, 1796, 1267, 3929, 2791, 1910, 891, 9719, 6057, 687, 77, 7127, 5936, 7197, 8830, 8178, 7233, 4722, 795, 6476, 3695, 5665, 4571, 9648, 5244, 4243, 6384, 7124, 8086, 454, 4980, 1657, 7213, 9934, 8566, 8296, 7505, 8330, 3830, 678, 4994, 1397, 9795, 7894, 1451, 6782, 4717, 3502, 4579, 5709, 6539, 8775, 606, 1973, 1681, 2408, 1056, 7187, 3250, 5952, 4354, 7750, 7083, 1921, 1815, 3632, 8689, 3537, 8370, 4293, 7306, 5847, 7740, 1000, 9404, 5959, 3447, 137, 8045, 7718, 6961, 4679, 766, 1145, 8218, 9582, 8853, 9818, 5680, 7730, 894, 3509, 1032, 8265, 4492, 4593, 3338, 2117, 9356, 6256, 7032, 7725, 4831, 9905, 1269, 9038, 7571, 757, 9009, 5491, 6975, 3994, 8869, 3074, 6397, 5797, 9437, 5982, 8385, 7215, 8497, 7916, 5382, 7356, 8815, 5059, 885, 3709, 9686, 7603, 3801, 367, 6844, 2979, 6958, 7412, 4169, 9055, 3155, 9711, 9237, 8913, 2868, 5339, 9777, 7310, 9200, 5762, 4858, 2594, 3104, 3724, 7769, 8785, 903, 2775, 9796, 3784, 2600, 6364, 5846, 869, 2288, 9453, 5876, 5000, 770, 2824, 1930, 9267, 7806, 359, 8760, 3749, 8992, 8817, 1060, 1355, 771, 2768, 491, 153, 7499, 1972, 4534, 5540, 7562, 4051, 3748, 6658, 3381, 1503, 6369, 7452, 453, 165, 6111, 4299, 264, 3909, 4576, 5546, 5447, 6666, 7845, 1057, 9512, 7653, 4979, 4430, 5746, 1536, 5568, 5016, 7010, 9929, 6598, 7532, 2264, 3223, 2938, 5704, 9863, 3778, 3531, 5834, 601, 4266, 8498, 1807, 1140, 7041, 2605, 1055, 2057, 5525, 1327, 5037, 4962, 1513, 5269, 9680, 9685, 6445, 355, 2786, 4735, 5302, 2081, 4622, 6095, 2320, 3785, 2535, 8224, 5310, 5321, 7724, 8617, 2392, 7983, 2055, 3107, 995, 3812, 2892, 7126, 2968, 1550, 9684, 229, 1543, 8984, 1453, 253, 7808, 7636, 3799, 9203, 4416, 2739, 3882, 1245, 5887, 4124, 3029, 4842, 6580, 2598, 9550, 9722, 4720, 716, 4794, 8761, 1404, 4918, 449, 1969, 6421, 7067, 641, 3174, 3571, 8772, 3698, 5685, 4143, 7517, 1844, 1841, 5798, 2035, 9868, 5086, 4446, 364, 1649, 5917, 6652, 3818, 697, 7842, 5259, 5095, 8280, 2000, 9119, 1076, 4596, 7105, 6366, 8018, 541, 7357, 6943, 4898, 990, 7531, 3946, 4676, 4039, 1636, 5228, 4656, 2643, 2954, 7886, 7026, 7764, 4546, 9127, 3187, 1544, 9247, 67, 675, 1643, 5639, 2471, 9623, 6916, 2772, 4523, 7495, 7536, 6332, 8403, 3456, 2513, 6944, 3578, 7609, 4365, 868, 1070, 5633, 1873, 3684, 5673, 2240, 4849, 1590, 7229, 5755, 5135, 4347, 3442, 213, 4789, 3715, 5331, 8598, 4761, 1084, 5276, 7140, 6798, 536, 7597, 124, 8940, 1253, 942, 5006, 8659, 773, 618, 6781, 8122, 3711, 3534, 1437, 3092, 1273, 4131, 9111, 1448, 4565, 234, 3551, 8562, 6608, 8499, 9220, 2151, 1086, 1725, 4985, 9145, 4839, 1763, 2692, 4938, 3952, 7909, 44, 971, 4139, 637, 5245, 7474, 9104, 4881, 7737, 6010, 1272, 4649, 6981, 4785, 4947, 5365, 8816, 7410, 8469, 4073, 2616, 3215, 789, 8031, 9063, 3299, 7268, 6312, 2179, 6255, 6904, 190, 8794, 8927, 9707, 4074, 6483, 4369, 8615, 2333, 977, 7345, 1692, 696, 966, 8653, 3199, 3346, 8819, 6626, 2986, 398, 7273, 9337, 3721, 790, 8824, 718, 1962, 4740, 5048, 8138, 5387, 8256, 7266, 6582, 2406, 4436, 8349, 8807, 4601, 12, 7973, 8161, 9739, 9421, 2425, 2446, 6714, 2131, 4210, 6733, 6738, 3444, 310, 591, 6587, 824, 1989, 5430, 4877, 3050, 2281, 6951, 592, 3052, 122, 5634, 4422, 941, 5080, 9105, 596, 271, 4479, 1906, 1792, 1475, 8558, 3054, 7221, 3143, 9098, 3545, 798, 7064, 3462, 2082, 4485, 635, 8379, 8674, 5177, 5758, 9820, 6910, 2942, 2185, 7423, 6230, 7836, 1887, 3153, 8493, 7906, 3699, 6938, 7050, 3156, 4566, 4806, 3236, 2609, 1587, 2663, 9130, 8837, 5725, 5582, 6422, 9385, 1264, 4682, 4961, 4891, 7042, 1698, 6806, 391, 9664, 2181, 7472, 8131, 2503, 6330, 1458, 4356, 9699, 9185, 8199, 6665, 7962, 5922, 2745, 41, 2823, 7392, 6307, 1661, 3488, 2518, 8742, 5548, 4382, 4200, 8622, 6208, 168, 7889, 9803, 723, 1219, 8120, 7774, 1483, 3212, 2336, 3977, 2263, 1307, 895, 1471, 7516, 9455, 2615, 9846, 1146, 7178, 9496, 1406, 962, 3204, 189, 9594, 3771, 300, 6222, 6192, 9500, 7444, 5567, 5614, 3448, 26, 9667, 8876, 5255, 8439, 1042, 8718, 3038, 9158, 3602, 4684, 5366, 7031, 4366, 873, 1168, 2963, 9094, 3779, 2227, 4006, 2133, 9033, 2344, 627, 1953, 2816, 7479, 6568, 4311, 4669, 4312, 5733, 6248, 2763, 1023, 6801, 8331, 792, 9633, 2214, 2316, 671, 8919, 2220, 5569, 1949, 92, 8719, 63, 875, 6987, 2125, 7346, 5011, 3078, 9635, 1385, 3451, 6564, 8809, 7176, 1308, 9007, 6449, 1172, 7960, 6868, 8006, 6635, 7890, 8971, 3809, 204, 3159, 2084, 9451, 4173, 2150, 4838, 3255, 8534, 947, 5042, 6325, 9595, 3998, 7771, 1031, 9761, 8629, 4072, 3983, 3944, 2142, 859, 761, 9091, 5775, 2628, 403, 7462, 725, 353, 3572, 9115, 3641, 452, 8707, 5241, 1364, 9833, 7248, 2785, 740, 515, 2527, 5774, 8793, 7235, 1390, 9553, 9870, 9159, 3126, 1843, 1719, 4737, 435, 8559, 2521, 3195, 3881, 8167, 4462, 2120, 3405, 6773, 1516, 3918, 6287, 2271, 5518, 8304, 8862, 9093, 6572, 3285, 1049, 9637, 3658, 1820, 9479, 4443, 8456, 533, 2981, 5584, 9805, 3924, 992, 2822, 3896, 6080, 4323, 2473, 6195, 4535, 4284, 6003, 1648, 4423, 2705, 5841, 6644, 6331, 1052, 1224, 415, 2108, 6090, 2576, 2741, 6968, 1915, 2691, 6726, 4328, 2800, 2919, 1998, 3063, 9435, 1975, 8283, 3164, 2448, 8038, 3426, 3276, 7146, 8288, 2865, 2795, 7451, 4221, 7751, 9518, 9443, 1927, 4431, 1776, 6715, 6119, 8216, 4914, 411, 7110, 2340, 732, 4265, 5352, 2048, 4372, 82, 8592, 4429, 8042, 8650, 5047, 3337, 309, 1009, 6117, 9856, 6867, 3004, 4763, 6158, 9611, 8440, 1823, 2712, 3840, 1814, 2749, 2110, 3680, 4592, 5392, 623, 7683, 1838, 5342, 5328, 30, 5779, 5198, 6600, 3635, 7191, 3549, 6107, 4063, 98, 4045, 9160, 3565, 6647, 3601, 1159, 235, 7493, 9193, 7643, 9076, 6668, 7463, 4457, 7363, 9728, 829, 4777, 9290, 1991, 5246, 2303, 7811, 5353, 3959, 1578, 2717, 1967, 6988, 1074, 59, 9612, 9872, 226, 3794, 8999, 312, 1310, 8522, 6778, 3520, 5305, 4401, 1813, 5273, 8297, 6845, 418, 2753, 9005, 6409, 7839, 1195, 1094, 5457, 3243, 8014, 3558, 830, 4971, 7121, 4660, 6583, 3905, 3262, 6353, 7667, 2511, 8568, 2487, 7182, 4681, 9857, 7741, 1523, 2555, 7263, 2420, 9097, 9389, 5281, 273, 7970, 9694, 3548, 180, 233, 2387, 4633, 9279, 3010, 4402, 4220, 3757, 8525, 1391, 9867, 4395, 3300, 9370, 8276, 4011, 2931, 8044, 4285, 3138, 5243, 485, 1810, 7980, 7614, 2638, 315, 6370, 8089, 3039, 920, 7605, 4260, 8411, 6996, 4371, 9631, 9399, 9172, 557, 4018, 9434, 3898, 7437, 1126, 2629, 8929, 1499, 2803, 1382, 5953, 2424, 2695, 4906, 1789, 714, 6283, 3489, 9825, 457, 2161, 9461, 735, 6630, 8950, 9470, 1331, 333, 6211, 93, 9498, 8446, 4868, 2445, 2135, 6098, 1621, 4198, 5880, 5653, 1122, 2298, 123, 6631, 2807, 9474, 784, 8050, 7731, 9020, 4450, 7230, 7225, 5490, 7611, 3860, 717, 3710, 9196, 88, 9610, 9002, 1558, 8805, 2444, 701, 9543, 258, 3113, 8544, 630, 9157, 6462, 9907, 3975, 3168, 7427, 918, 9658, 9783, 4032, 236, 4752, 5438, 3933, 626, 500, 7792, 6796, 6894, 2965, 5485, 695, 8510, 1983, 5210, 4330, 2948, 6206, 8020, 3776, 8736, 1043, 9862, 9433, 2861, 5714, 1571, 7795, 9494, 767, 6219, 6914, 5378, 8933, 2061, 8005, 603, 2076, 5112, 604, 4437, 6620, 6105, 5810, 5134, 9190, 7425, 7511, 6898, 9416, 9352, 8998, 9330, 6045, 8714, 7858, 7781, 6472, 5950, 4668, 6872, 7103, 1087, 8763, 4239, 5349, 2095, 6538, 6067, 912, 9006, 2947, 9238, 6160, 4225, 4206, 1030, 412, 6697, 8384, 4827, 3431, 2180, 7568, 2660, 6439, 4555, 8915, 1257, 5895, 6036, 4724, 1833, 3557, 9661, 3591, 5703, 7319, 9082, 5299, 6493, 1890, 2030, 843, 83, 4958, 9283, 5699, 4594, 433, 1029, 7240, 6595, 9300, 1522, 467, 5172, 6454, 6132, 5573, 1716, 6851, 2992, 8090, 5671, 5072, 5631, 8231, 1231, 5463, 9153, 1511, 6889, 4879, 2402, 7616, 6835, 3323, 7210, 103, 4228, 2592, 2423, 5606, 4843, 2233, 4108, 2260, 101, 4024, 2235, 2688, 7783, 1766, 388, 8636, 5369, 4427, 5045, 5443, 6377, 5780, 3189, 1828, 51, 6333, 5521, 5313, 5106, 7393, 13, 9085, 8867, 5558, 9133, 827, 8846, 5867, 2653, 4692, 7940, 2242, 1277, 6676, 1493, 526, 7634, 7223, 9047, 5893, 2922, 8991, 7647, 4001, 8502, 7645, 3652, 4493, 8479, 6753, 5629, 2456, 4174, 5145, 4970, 5718, 9592, 7239, 2961, 8822, 2631, 6481, 3499, 4000, 4035, 4287, 7094, 6150, 1210, 2873, 2964, 2517, 7214, 5851, 7982, 3872, 2781, 140, 2713, 6688, 3540, 4012, 4386, 4107, 8692, 4331, 6052, 7257, 1416, 4454, 5024, 5721, 8618, 1804, 1834, 5499, 6786, 7150, 9827, 9571, 2764, 1711, 5863, 8207, 5450, 6270, 5388, 1417, 8872, 2265, 7237, 4470, 6419, 382, 7378, 900, 7871, 8481, 3183, 8448, 1452, 5786, 2139, 3539, 6609, 2236, 5792, 6953, 6589, 7717, 8871, 9547, 1774, 8269, 1943, 6671, 3371, 9688, 7292, 19, 7154, 3850, 6520, 3786, 1449, 5081, 8985, 4116, 6972, 8371, 7855, 9789, 6873, 172, 9655, 6108, 586, 5287, 5652, 8538, 7874, 4896, 2682, 3728, 6695, 9486, 7486, 4003, 1929, 2625, 9937, 8418, 5416, 8196, 7335, 8294, 4235, 7514, 8906, 5335, 3095, 8353, 7447, 4631, 2015, 117, 6915, 8836, 2927, 9563, 292, 3485, 3671, 9503, 9940, 8654, 3198, 9064, 3612, 1798, 6707, 8492, 2018, 4648, 5809, 8936, 6995, 3247, 5301, 8046, 6510, 5806, 8187, 6023, 7800, 622, 9226, 9348, 7297, 9103, 4711, 9114, 7702, 9184, 1651, 5309, 5643, 8696, 4691, 4798, 4773, 9534, 3874, 8464, 726, 7070, 3653, 4654, 3907, 58, 1467, 4374, 2274, 7355, 187, 350, 5357, 4564, 8988, 595, 7654, 3316, 1706, 3084, 5511, 1958, 1795, 8290, 6599, 1303, 6982, 1113, 804, 9311, 7374, 1297, 9616, 6017, 4619, 169, 9589, 2261, 8995, 9257, 3487, 3566, 1871, 8252, 7967, 8174, 9026, 677, 5911, 2312, 4677, 1885, 5522, 9473, 580, 8845, 1301, 3493, 736, 5983, 6273, 5052, 2565, 7914, 8903, 4755, 3514, 8540, 4387, 2767, 1585, 1132, 7348, 3654, 8262, 628, 5423, 1794, 5202, 5381, 9210, 9740, 6716, 4568, 8285, 2529, 2065, 720, 8973, 7316, 8818, 5182, 4907, 4643, 1175, 9293, 5039, 6093, 9738, 1870, 3005, 7380, 4491, 6881, 4277, 330, 7280, 5429, 2483, 4575, 6394, 5236, 638, 9459, 5785, 2195, 5742, 1067, 6128, 6614, 9241, 907, 8531, 5161, 2836, 4009, 6789, 1302, 1748, 6338, 8550, 9019, 2672, 257, 6309, 3057, 8078, 7630, 882, 7034, 5860, 5799, 1158, 8397, 8427, 5609, 8317, 7644, 7036, 2294, 4683, 5656, 3418, 5612, 1608, 5025, 1254, 107, 2611, 2356, 4351, 1468, 9762, 5073, 9229, 4553, 3814, 5445, 7403, 651, 8944, 679, 4115, 1773, 3885, 6357, 9092, 3269, 8752, 9670, 7286, 6356, 7513, 17, 8739, 8852, 5997, 3217, 5769, 2074, 1696, 484, 8081, 5632, 2004, 5137, 3954, 6850, 8355, 8447, 105, 8234, 2216, 5347, 4792, 2107, 6891, 6574, 8669, 6521, 9342, 7385, 3378, 4584, 1817, 5060, 1329, 2201, 2687, 8281, 4147, 1971, 3458, 126, 4188, 7898, 6213, 5676, 3926, 710, 8645, 9446, 905, 8832, 8402, 4910, 2853, 3681, 9427, 9584, 1282, 9797, 6039, 8030, 1455, 7569, 3611, 7972, 9154, 1289, 8583, 7881, 6698, 313, 3080, 5691, 974, 4238, 6925, 2626, 9799, 3956, 1534, 6440, 7607, 5386, 6888, 5481, 8076, 6157, 1440, 7768, 7698, 8708, 3930, 8273, 9117, 8868, 304, 3233, 9883, 6284, 1171, 9244, 6399, 9840, 2138, 4709, 5439, 8240, 5964, 8571, 8339, 6913, 5988, 5820, 5492, 7135, 2104, 3158, 7148, 3524, 3991, 4852, 6221, 8843, 3740, 3922, 9903, 544, 8518, 1280, 4049, 9916, 259, 9032, 3076, 6156, 4088, 4030, 744, 463, 7203, 9271, 9511, 2560, 787, 9588, 727, 2590, 2103, 4841, 4778, 3096, 6172, 5221, 8052, 8727, 1667, 7058, 7305, 8519, 3397, 4644, 7096, 8693, 9071, 9054, 7587, 2978, 7019, 7883, 6578, 4168, 2287, 7492, 3383, 5992, 145, 3386, 2159, 2461, 2704, 2827, 5562, 455, 6489, 2559, 4990, 5504, 2760, 4203, 863, 9315, 5937, 4510, 4670, 3871, 6692, 7418, 877, 4079, 9690, 72, 2991, 8037, 9448, 3766, 5602, 4481, 4234, 1192, 7762, 6190, 5565, 5636, 4917, 227, 524, 2286, 8129, 922, 4406, 8373, 4066, 9800, 1599, 1268, 8783, 3070, 53, 1879, 2289, 112, 3399, 6259, 1914, 3348, 1, 4874, 7508, 2115, 3464, 7502, 7407, 4940, 8757, 9384, 6899, 8792, 7557, 9836, 177, 5427, 980, 246, 5655, 8154, 8301, 206, 1138, 7809, 1164, 3686, 8145, 1346, 9298, 6940, 2996, 8716, 7974, 3259, 4083, 5520, 4338, 6275, 2889, 8580, 2710, 6758, 1454, 5121, 2974, 4400, 40, 9517, 8289, 2900, 9149, 8409, 9366, 3288, 3843, 2285, 1415, 9000, 80, 4087, 4098, 7071, 7013, 3140, 7672, 7617, 9361, 2750, 5251, 3981, 7652, 5783, 5840, 1429, 4359, 442, 4984, 6854, 6606, 74, 7025, 6827, 1753, 9735, 3280, 7087, 9514, 9749, 6181, 8230, 9363, 6656, 3334, 5215, 9170, 1123, 4465, 6426, 9618, 3146, 682, 1423, 5638, 6491, 6403, 6820, 1996, 6586, 4348, 4819, 6349, 6717, 8643, 6387, 9422, 8152, 3466, 9397, 7485, 8935, 3597, 8450, 4490, 3958, 867, 9604, 1400, 3305, 8881, 9576, 4339, 3392, 8056, 4797, 7394, 6503, 4261, 940, 6548, 2164, 1539, 7343, 925, 2348, 7772, 7255, 7601, 9478, 1240, 1230, 1072, 2777, 1150, 4835, 8261, 5910, 5220, 9039, 7107, 4824, 519, 5120, 2353, 8552, 1717, 9521, 7966, 2198, 5133, 161, 8158, 5662, 3992, 269, 1486, 5527, 3553, 5865, 9625, 4937, 8756, 6245, 6441, 8939, 6037, 8628, 3271, 9236, 3101, 2878, 4196, 2782, 2793, 1641, 4411, 9640, 8675, 813, 8857, 1891, 87, 6321, 6523, 8193, 1547, 7856, 260, 492, 3257, 853, 2599, 8619, 2632, 1162, 9851, 4509, 8977, 3517, 5118, 7358, 3884, 4433, 9029, 8338, 7633, 4703, 9110, 6736, 2534, 8367, 3836, 162, 7615, 636, 9574, 7975, 3584, 7023, 8211, 5232, 8077, 4425, 676, 663, 7796, 7846, 2027, 7021, 6934, 7061, 8054, 693, 6358, 6672, 7389, 7179, 3888, 7227, 8994, 6634, 3844, 2929, 3852, 8644, 6576, 3478, 6418, 1892, 6546, 8106, 9564, 3354, 3402, 3184, 5523, 9355, 9165, 7612, 8001, 6432, 4562, 4846, 2612, 4199, 2729, 108, 4911, 8070, 8663, 3132, 5279, 1012, 3510, 5044, 4448, 7224, 8380, 5180, 9056, 7910, 6193, 952, 420, 3857, 3980, 3375, 9075, 5110, 2621, 3608, 2489, 2432, 6274, 8728, 9824, 2542, 4780, 9334, 247, 6855, 6091, 7736, 9613, 7661, 8652, 8064, 1986, 8576, 4268, 3747, 6711, 5590, 3298, 9570, 9718, 509, 513, 3015, 5370, 2347, 5918, 5452, 2867, 5262, 9607, 8449, 8941, 7168, 2452, 5009, 9128, 6618, 4415, 9364, 801, 9821, 4246, 8401, 9717, 9858, 892, 5575, 8303, 7707, 4721, 5098, 3460, 4950, 9147, 7366, 423, 8260, 6949, 9662, 8023, 3875, 9249, 2007, 6840, 1445, 7854, 9743, 3388, 6344, 6099, 594, 4156, 8047, 590, 6512, 9771, 8524, 1946, 6928, 9619, 9702, 1734, 8134, 6289, 4044, 8513, 4966, 7506, 3225, 1687, 4804, 5872, 914, 4134, 2443, 3787, 5155, 7288, 1444, 3167, 2661, 7671, 9251, 4023, 951, 8151, 4784, 9001, 3073, 192, 6677, 6879, 4861, 9487, 956, 1788, 2721, 1609, 2086, 7027, 9375, 8358, 1799, 9918, 2069, 1863, 6383, 5945, 7054, 7232, 4167, 1360, 6859, 1976, 9838, 9466, 2515, 3290, 4004, 7570, 7876, 3396, 9578, 857, 7810, 8083, 2272, 3990, 4186, 7455, 7639, 288, 5524, 9591, 8611, 615, 5757, 9202, 2790, 6461, 1351, 3400, 9501, 3249, 3406, 7850, 8526, 8389, 6924, 8788, 6004, 3287, 5513, 5986, 3943, 3320, 8097, 2657, 3731, 2756, 1944, 8838, 4010, 1202, 5537, 81, 4662, 5772, 1821, 2225, 9531, 5291, 4279, 5480, 1154, 2437, 5864, 185, 8458, 3687, 2918, 5214, 6536, 2189, 3725, 7662, 7648, 3441, 6569, 4960, 6720, 5926, 4767, 9559, 570, 9715, 4818, 8635, 1353, 5114, 5587, 2502, 2944, 7711, 1936, 821, 2368, 9544, 3573, 7551, 7920, 2574, 133, 3218, 4461, 5702, 8300, 385, 4332, 2969, 8894, 6511, 5185, 2912, 8320, 7598, 9533, 7566, 6979, 2496, 7685, 6577, 7689, 2510, 7009, 3821, 8626, 178, 4301, 6749, 9354, 2516, 4600, 62, 1189, 8839, 6027, 7106, 2720, 5781, 9696, 6771, 2917, 3615, 3648, 1646, 8722, 4607, 9891, 3993, 5877, 2630, 3583, 4302, 158, 9173, 6682, 709, 3717, 8471, 6649, 1548, 7999, 4982, 255, 2727, 4609, 7473, 5990, 633, 4766, 1758, 4897, 4081, 6246, 9394, 102, 5272, 8166, 2932, 6189, 4458, 6783, 5384, 6063, 1978, 5690, 283, 1875, 1111, 5760, 5615, 504, 7882, 303, 2013, 5178, 183, 4397, 9745, 685, 8834, 8136, 8259, 9, 8641, 9669, 1001, 3867, 1487, 5507, 5359, 9045, 8153, 7416, 4421, 5822, 1961, 8893, 3577, 9118, 9577, 4859, 3507, 4802, 3586, 3892, 8529, 9901, 6000, 5873, 9714, 9657, 2167, 8909, 5406, 7084, 1215, 1574, 3045, 1521, 7498, 3009, 4280, 8102, 4257, 6145, 7635, 6214, 4407, 938, 7066, 3923, 7065, 7756, 9502, 9048, 4464, 27, 808, 1931, 8473, 7538, 6005, 8588, 7481, 6186, 7014, 3999, 4883, 6790, 7006, 5332, 2001, 2980, 4933, 1529, 5351, 1934, 1669, 3206, 2457, 6785, 4019, 6710, 3664, 1878, 1658, 4233, 5650, 6892, 7669, 2617, 6645, 7049, 2714, 6984, 556, 1700, 2228, 3281, 3129, 1119, 5626, 9808, 2436, 2864, 6495, 7992, 3176, 8734, 4760, 4756, 470, 6839, 6341, 7893, 4948, 8607, 2872, 8627, 9850, 9121, 3264, 5085, 9691, 9194, 5980, 3592, 3055, 6818, 3090, 3481, 899, 583, 8918, 7885, 6177, 1623, 8413, 5939, 390, 4434, 9456, 5831, 5956, 2252, 611, 9262, 7330, 8321, 6412, 5608, 9529, 5869, 1441, 90, 4788, 6929, 3506, 1593, 7040, 200, 6565, 8966, 7161, 7169, 919, 9736, 5814, 1018, 6121, 429, 5985, 7177, 3523, 4097, 1977, 6832, 1994, 1897, 9925, 6239, 983, 5373, 9357, 6878, 284, 2363, 9125, 7004, 8840, 4297, 4227, 7925, 3544, 8600, 1854, 1556, 5067, 7803, 5829, 7413, 6209, 6015, 7681, 9084, 731, 97, 7327, 1726, 8237, 1553, 4639, 3533, 5362, 7077, 5460, 4255, 4059, 8036, 5158, 8286, 6161, 1478, 2953, 3139, 4329, 209, 3772, 8877, 5993, 6895, 1665, 4923, 1802, 555, 5036, 6173, 6146, 5160, 9174, 774, 4628, 3547, 7853, 1723, 3193, 7936, 3940, 118, 4191, 5026, 5385, 4618, 5176, 9900, 3463, 4611, 8738, 1816, 7673, 691, 377, 9932, 7334, 2175, 8186, 2205, 1011, 9810, 6765, 3744, 1580, 5727, 6799, 3051, 4701, 1021, 2593, 8359, 4204, 1586, 5304, 2911, 4747, 9549, 4964, 4518, 2166, 5657, 8671, 1083, 525, 9599, 8215, 7604, 880, 487, 9632, 5712, 1537, 647, 3331, 7553, 6088, 2648, 4499, 1617, 8104, 5449, 7206, 5991, 9700, 764, 375, 3732, 5622, 5476, 5695, 422, 8073, 3020, 4144, 426, 7519, 4441, 2725, 4527, 3868, 3596, 542, 1764, 5292, 8990, 9216, 7445, 3201, 1109, 3034, 290, 5857, 1721, 4399, 6125, 7678, 6118, 3925, 5923, 2588, 2389, 3379, 6556, 5596, 1069, 539, 1947, 7056, 5854, 6923, 8470, 1412, 6547, 4955, 9417, 7875, 4267, 3048, 6453, 3647, 6581, 7167, 6203, 2492, 8767, 6009, 1894, 4762, 5424, 8664, 4541, 2046, 648, 8204, 6919, 9780, 6106, 9405, 7080, 4617, 1507, 8094, 1407, 2097, 1213, 5912, 8364, 7753, 9088, 61, 2943, 2554, 9853, 8007, 562, 8264, 8921, 1840, 7073, 8864, 1563, 1115, 7868, 4251, 427, 7011, 7790, 4825, 5906, 3182, 6400, 1293, 5975, 6083, 5062, 4882, 2993, 3659, 8197, 1461, 4218, 2664, 7728, 210, 1206, 4903, 2438, 1781, 2152, 9161, 5844, 4384, 579, 8545, 8357, 4708, 216, 5927, 9877, 3367, 9888, 7679, 5149, 6985, 9683, 9855, 2562, 3605, 4455, 451, 9695, 5233, 8967, 141, 9630, 2480, 2788, 1510, 9272, 7466, 6775, 4264, 1938, 8905, 6584, 6310, 9240, 9866, 5261, 1250, 8243, 5960, 9335, 3911, 9924, 6056, 5164, 2462, 3820, 1624, 4741, 6768, 7274, 338, 3614, 4058, 9597, 163, 5346, 3970, 2145, 8435, 3258, 7091, 5940, 575, 7, 2639, 6002, 1508, 1233, 1790, 9388, 9546, 1750, 4037, 1425, 3603, 501, 9822, 498, 3838, 5442, 7086, 8569, 7409, 4736, 8096, 8345, 3626, 8071, 6226, 3527, 7298, 5882, 244, 8028, 4563, 6540, 760, 9499, 4414, 6089, 9569, 3829, 5707, 9189, 1675, 2393, 6563, 1266, 1859, 2881, 8997, 2779, 6110, 23, 5456, 1812, 5107, 5534, 4800, 3293, 5853, 719, 1199, 8681, 1506, 2876, 3319, 1180, 6502, 2651, 3804, 9440, 2851, 2675, 1211, 9126, 4902, 8191, 8421, 619, 9319, 8660, 928, 4474, 4075, 1474, 1697, 5571, 7095, 2558, 99, 8740, 6329, 4137, 6766, 4216, 4727, 7767, 9609, 6386, 9186, 5109, 5278, 6986, 9484, 3636, 5224, 9132, 5018, 1306, 2798, 831, 3302, 7884, 1679, 7976, 1806, 2080, 7500, 5754, 4884, 1695, 1053, 9801, 9705, 5166, 8535, 5931, 4557, 8455, 1078, 3342, 4306, 9539, 3902, 1546, 2210, 715, 7927, 8799, 8267, 8072, 2399, 5323, 2569, 1783, 8287, 9177, 9703, 2415, 2792, 4029, 8655, 7879, 5054, 9218, 9704, 6435, 3713, 121, 2557, 8557, 8670, 7580, 323, 8322, 8315, 9234, 2613, 5116, 7208, 1024, 9004, 275, 8350, 8970, 3927, 7507, 9792, 6667, 2174, 4135, 2743, 943, 3192, 9875, 6492, 9606, 953, 3449, 9245, 9730, 208, 4185, 3774, 5858, 7008, 5828, 3099, 370, 1142, 4522, 18, 7619, 5441, 7592, 8475, 1343, 8366, 7430, 2701, 9605, 849, 4, 6450, 6705, 3676, 1644, 5539, 7435, 2037, 2849, 7063, 2796, 2585, 929, 8901, 3560, 3579, 1286, 2470, 1678, 175, 9228, 1613, 5038, 4172, 3729, 8253, 8155, 2509, 5740, 2297, 3620, 2230, 7892, 57, 8500, 4031, 8375, 5325, 2126, 9231, 3461, 2217, 6812, 9876, 5932, 3622, 9902, 6602, 5674, 7978, 7134, 8229, 7125, 1414, 2776, 2416, 1990, 7522, 1443, 7329, 5649, 3483, 5409, 6567, 786, 1731, 5468, 4360, 341, 5437, 3137, 7542, 4685, 3656, 6040, 2698, 4635, 5694, 6947, 7572, 9187, 410, 3541, 2172, 6784, 8553, 9568, 8057, 4106, 7663, 7005, 1259, 5290, 850, 2143, 5955, 4655, 5628, 9227, 5317, 1003, 52, 3180, 8917, 4837, 8316, 5819, 3035, 3087, 5528, 3062, 6264, 139, 2656, 6744, 921, 6954, 2928, 335, 2587, 5089, 8356, 6317, 2282, 9263, 6152, 3191, 7284, 8947, 2934, 5364, 6008, 6730, 8774, 7865, 9505, 3385, 560, 5194, 2696, 9787, 2724, 2218, 9144, 1300, 9837, 152, 8466, 4122, 2732, 9465, 6295, 8441, 7173, 8758, 9520, 5489, 7680, 3997, 4710, 3136, 7258, 1855, 2684, 3835, 4036, 5414, 5289, 1512, 1549, 7320, 1557, 1979, 8017, 7560, 1993, 1999, 1066, 5399, 5588, 2388, 7905, 4232, 9794, 7804, 1081, 1340, 3965, 5285, 1127, 5108, 8596, 7870, 1401, 5741, 135, 9482, 7666, 302, 48, 9831, 3518, 597, 6772, 8491, 5619, 6479, 4986, 3694, 7454, 4659, 1088, 4373, 3205, 9557, 5710, 752, 1980, 2619, 9180, 8848, 320, 6413, 4442, 9689, 345, 4753, 4718, 3525, 3230, 1402, 6215, 439, 7283, 3098, 76, 759, 7461, 1830, 3617, 5659, 5477, 1312, 6470, 2342, 5007, 219, 1418, 7701, 3128, 9400, 8797, 7185, 2655, 9058, 4056, 6187, 2130, 2411, 3666, 1957, 810, 9528, 7489, 8472, 3864, 8541, 7954, 2060, 1284, 2165, 6627, 5516, 1368, 4140, 7388, 8938, 631, 6136, 6998, 314, 5547, 3401, 6360, 9057, 681, 3650, 8051, 4696, 6518, 5296, 7650, 5576, 3227, 8632, 6306, 858, 8123, 3730, 2906, 2497, 4123, 5784, 9659, 8856, 4646, 1241, 2539, 3960, 8016, 5256, 9644, 1481, 6734, 1622, 7069, 5764, 6709, 96, 7376, 6681, 3066, 4805, 2603, 965, 5816, 7625, 176, 4038, 6674, 5519, 2077, 6032, 799, 7656, 4231, 9333, 5286, 113, 7777, 8029, 883, 9219, 7518, 8459, 5428, 4845, 8015, 1133, 380, 4244, 1708, 3365, 3825, 6031, 8114, 3149, 5213, 2243, 174, 1177, 4875, 5216, 6240, 2976, 3425, 6466, 4078, 1565, 763, 1065, 5550, 458, 6962, 7068, 6882, 8773, 8683, 3147, 7060, 2773, 64, 4092, 5128, 7782, 5595, 3901, 9321, 1006, 2814, 3964, 6133, 1372, 2269, 6339, 6886, 8850, 4680, 2747, 3019, 6075, 4975, 9288, 886, 6135, 7090, 4713, 6059, 7695, 6134, 9497, 5578, 6297, 6086, 6490, 9767, 6257, 3737, 8480, 1660, 4512, 7424, 4283, 4856, 111, 7512, 9572, 5288, 1117, 4714, 4047, 474, 6327, 8710, 5874, 4623, 119, 9894, 4870, 5253, 1457, 6142, 7852, 5826, 9369, 1730, 9166, 3018, 2490, 241, 2381, 4935, 6592, 8060, 5795, 5471, 6373, 1097, 4154, 3559, 3762, 5169, 9651, 8374, 3322, 8860, 4925, 659, 4254, 9425, 9255, 8238, 802, 115, 5903, 201, 8958, 2258, 3272, 9013, 1755, 8214, 5825, 5484, 2520, 3372, 9101, 8272, 4864, 3862, 5422, 8651, 2977, 4650, 8065, 4517, 3670, 3505, 4909, 7744, 4967, 3657, 4453, 5974, 8333, 9100, 1555, 8334, 1688, 2738, 4440, 5270, 6813, 7686, 1836, 1393, 8251, 3631, 5448, 4951, 9383, 9823, 6033, 2716, 8753, 751, 2380, 1156, 8697, 6001, 7766, 1229, 5642, 9449, 3469, 9593, 5526, 8743, 1737, 7293, 1323, 5074, 4094, 9629, 4318, 8, 9731, 2375, 8394, 8426, 1715, 3120, 7200, 2169, 5141, 7249, 1743, 4494, 5131, 85, 4712, 1981, 9791, 2377, 3260, 625, 3332, 3453, 503, 5883, 413, 4556, 4326, 5811, 9235, 4552, 9432, 9752, 436, 3000, 2468, 2635, 8625, 2858, 8377, 8125, 6562, 2722, 3491, 2279, 4725, 5794, 4969, 2478, 3971, 7360, 6993, 1713, 7606, 6809, 4160, 654, 5979, 5807, 7483, 1035, 5796, 2493, 930, 3185, 994, 7081, 249, 8677, 8841, 1554, 4117, 1139, 7600, 9758, 8932, 5057, 2440, 2531, 3457, 217, 8249, 8516, 5843, 4924, 6389, 2532, 6224, 8087, 1036, 2002, 552, 6704, 8142, 6876, 4893, 5693, 1234, 6648, 5199, 1803, 8706, 160, 1625, 7595, 9412, 9287, 2364, 5218, 9060, 1479, 6542, 8537, 4375, 7043, 1276, 7545, 1198, 471, 588, 9371, 3515, 5254, 5104, 7395, 49, 5225, 9143, 8022, 60, 5995, 3855, 2362, 3356, 8003, 143, 3880, 6115, 1341, 4290, 2665, 5267, 7130, 9580, 4640, 8928, 5954, 7658, 5136, 5958, 1709, 7328, 5720, 4300, 3968, 2043, 6012, 4569, 9368, 2544, 3413, 6991, 4992, 1932, 4886, 3511, 5070, 130, 1275, 186, 4308, 9260, 5981, 8363, 4008, 6127, 89, 4853, 1881, 8679, 3232, 9349, 1572, 7079, 8407, 743, 3542, 4638, 9430, 3593, 4999, 7743, 3231, 5751, 4355, 9280, 5314, 5028, 5713, 3665, 756, 2254, 5193, 910, 7895, 8476, 3675, 2349, 116, 7475, 6653, 2706, 6751, 960, 9712, 2378, 4025, 128, 6285, 7399, 6467, 1354, 8430, 6948, 828, 3127, 4288, 2855, 4511, 1376, 2223, 4700, 9468, 5812, 8144, 4157, 1888, 1357, 7835, 2367, 7002, 9346, 5217, 4560, 9887, 9304, 5696, 3427, 4530, 5488, 7555, 1367, 9328, 1151, 6065, 8271, 6178, 517, 2147, 9671, 4136, 1413, 5660, 9066, 395, 5616, 8381, 576, 7458, 3446, 2925, 1311, 285, 4796, 937, 197, 574, 1218, 3475, 8646, 7544, 5788, 976, 600, 2358, 2202, 2983, 7370, 4597, 923, 9896, 7436, 5530, 3123, 4916, 3041, 981, 5097, 4410, 1026, 6395, 6081, 9112, 4888, 9028, 4377, 2564, 3594, 5951, 7851, 3535, 43, 505, 9124, 4258, 2581, 4602, 7012, 4335, 20, 4627, 1263, 3118, 9579, 3637, 2041, 5663, 3963, 2200, 5191, 893, 4121, 9726, 5389, 6122, 4368, 7296, 2222, 1569, 713, 2156, 4077, 7958, 2277, 2056, 7965, 444, 4120, 2916, 807, 4549, 1442, 1100, 79, 4418, 6550, 7593, 5031, 8983, 9737, 6780, 8874, 6402, 5962, 4224, 6448, 548, 6852, 4657, 4528, 9314, 2325, 6167, 7515, 421, 7998, 4379, 2988, 2433, 2016, 4250, 7703, 7537, 1176, 5266, 4394, 2255, 8257, 593, 202, 4305, 1530, 9681, 9565, 7219, 8165, 1362, 9086, 2234, 9268, 2124, 3297, 8084, 9472, 2737, 5327, 9899, 7055, 3979, 7903, 9909, 1214, 1384, 5881, 4632, 3951, 6487, 5358, 8699, 8118, 5230, 8137, 2553, 2506, 181, 7340, 8092, 3252, 6825, 9567, 7657, 6917, 2191, 9927, 5400, 8754, 5283, 3275, 4836, 212, 6959, 9773, 9663, 5989, 9419, 5929, 5393, 573, 9270, 4113, 8735, 6558, 1296, 5684, 7584, 2153, 294, 1880, 1185, 47, 4420, 5557, 5641, 7278, 2318, 6305, 6035, 4963, 5130, 9212, 4363, 8963, 3660, 3404, 4876, 414, 6763, 9859, 6887, 1096, 6130, 7136, 800, 7628, 4248, 5356, 3854, 1426, 5830, 8678, 6300, 705]

with open('../DATA/person_id/train_list.pkl', 'wb') as f:
    pickle.dump(train_list, f)

