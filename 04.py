price_tv = 9000
price_dvd = 2250
price_audio = 4500

num_tv = int(input('How many TVs do you want? '))
num_dvd = int(input('How many DVD players do you want? '))
num_audio = int(input('How many audio systems do you want? '))

total = num_tv*price_tv + num_dvd*price_dvd + num_audio*price_audio

print('Total price is',"{:.2f}".format(total),'baht.')

if total >= 30000 :
    discount = 0.05
    print('You got a discount of',"{:.2f}".format(total*discount),'baht.')

else:
    discount = 0

print('Please pay',"{:.2f}".format(total - total*discount),'baht. Thank you very much.')

