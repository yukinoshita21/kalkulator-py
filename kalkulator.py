ulang = True

while ulang:

          print('program kalkulator sederhana')

          operasi = input('masukan operasi yang ingin anda lakukan (tambah,kurang,kali,bagi)= ')

          if operasi == 'tambah':
               
               tambah_1 = float(input('masukan bilangan 1= '))
               tambah_2 = float(input('masukan bilangan 2= '))
               
               hasil_tambah = tambah_1 + tambah_2
               
               print(f'hasil {tambah_1} ditambah {tambah_2} adalah {hasil_tambah}')
              
          elif operasi == 'kurang':
               
               kurang_1 = float(input('masukan bilangan 1= '))
               kurang_2 = float(input('masukan bilangan 2= '))
               
               hasil_kurang = kurang_1 - kurang_2
               
               print(f'hasil {kurang_1} dikurang {kurang_2} adalah {hasil_kurang}')
          elif operasi == 'kali':
               
               kali_1 = float(input('masukan bilangan 1= '))
               kali_2 = float(input('masukan bilangan 2= '))
               
               hasil_kali = kali_1 * kali_2
               
               print(f'hasil {kali_1} dikurang {kali_2} adalah {hasil_kali}')
          elif operasi == 'bagi':
               
               bagi_1 = float(input('masukan bilangan 1= '))
               bagi_2 = float(input('masukan bilangan 2= '))
               
               hasil_bagi = bagi_1 / bagi_2
               
               print(f'hasil {bagi_1} dikurang {bagi_2} adalah {hasil_bagi}')
          else:
               print('masukan operasi yang sesuai!!')
               
          lagi = input('Apakah Anda ingin mengulangi program? (ya/tidak): ')
          if lagi.lower() != 'ya':
               ulang = False
               print('Program telah selesai.')
               





