def main():
    #Createa a byte array
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    #Creating a string
    s = "string"
    print(s)
    
    #combining both
    # print(b+s)

    #Decoding bytes
    b2 = b.decode('utf=8')
    print(s+b2)

    #encoding string
    s2 = s.encode('utf-8')
    print(s2+b)

    #Encoding using utf-32
    s3 = s.encode("utf-32")
    print(s3)


if __name__ == "__main__":
    main()