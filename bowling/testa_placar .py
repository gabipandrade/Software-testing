#Gabriela Passos de Andrade - 12625142
#Rafael Cunha Bejes Learth -13676367
#Emanuel Percinio Gonçalves de Oliveira - 13676878
import os
os.system("python3 -m pyproteum testnew --D ./ placar")
os.system("python -m pyproteum tcase --add --D ./ --S funcional.py placar")
os.system("python -m pyproteum tcase --add --D ./ --S mcdc.py placar")
os.system("python -m pyproteum tcase --add --D ./ --S mutation.py placar")
#os.system("python -m pyproteum tcase --list --D ./  placar")
os.system("python -m pyproteum mutagen --create --D ./ --all 100 0 placar")
os.system("python -m pyproteum exemuta --equiv --D ./ --x '1066 1071 1076 1089 1094 1099 1104 1109  1114 1139 1144 1149 1154 1159 1164 1208' placar")
os.system("python -m pyproteum exemuta --equiv --D ./ --x '184 187 217 220 221 530 531 532 533 570 583 590 600 606 635 643 648 649 655 660 661 666 667 672 675 676 682 686 687 688 ' placar")
os.system("python -m pyproteum exemuta --equiv --D ./ --x '79 80 159 302 304 306 318 327 336 342 350' placar")
os.system("python -m pyproteum exemuta --equiv --D ./ --x '230 232 238 239 245 248 249 253 254 255 307 352 680 681 1049 1124' placar")
os.system("python -m pyproteum exemuta --exec --D ./ placar")
#os.system("python -m pyproteum mutaview --gui --D ./ placar")