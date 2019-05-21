# Caesar Cipher Hacker


message = '5coOMXXcoPSZIWoQI'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key:
for key in range(len(SYMBOLS)):
    # Important: set translated to ZERO after displaying every transtation with each key

    translated = ''

    # The rest is as Cypher

    # Loop through each symbol message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound. Vuelta al principio
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append symbol not encrypted/decrypted:
            translated = translated + symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
    # IMPORTANT: Use str FORMATING when joining INT + STRING
    # If we do it with + it won't work
