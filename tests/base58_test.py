# Copyright (c) 2020 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
import binascii
import unittest
from bip_utils import Base58Decoder, Base58Encoder


# Test vector from Bitcoin code tests
# https://github.com/bitcoin/bitcoin/blob/master/src/test/data/base58_encode_decode.json
TEST_VECTOR = \
    [
        {
            "raw"          : b"61",
            "encode"       :  "2g",
            "check_encode" :  "C2dGTwc"
        },
        {
            "raw"          : b"626262",
            "encode"       :  "a3gV",
            "check_encode" :  "4jF5uERJAK"
        },
        {
            "raw"          : b"636363",
            "encode"       :  "aPEr",
            "check_encode" :  "4mT4krqUYJ"
        },
        {
            "raw"          : b"73696d706c792061206c6f6e6720737472696e67",
            "encode"       :  "2cFupjhnEsSn59qHXstmK2ffpLv2",
            "check_encode" :  "BXF1HuEUCqeVzZdrKeJjG74rjeXxqJ7dW"
        },
        {
            "raw"          : b"00eb15231dfceb60925886b67d065299925915aeb172c06647",
            "encode"       :  "1NS17iag9jJgTHD1VXjvLCEnZuQ3rJDE9L",
            "check_encode" :  "13REmUhe2ckUKy1FvM7AMCdtyYq831yxM3QeyEu4"
        },
        {
            "raw"          : b"516b6fcd0f",
            "encode"       :  "ABnLTmg",
            "check_encode" :  "237LSrY9NUUas"
        },
        {
            "raw"          : b"bf4f89001e670274dd",
            "encode"       :  "3SEo3LWLoPntC",
            "check_encode" :  "GwDDDeduj1jpykc27e"
        },
        {
            "raw"          : b"572e4794",
            "encode"       :  "3EFU7m",
            "check_encode" :  "FamExfqCeza"
        },
        {
            "raw"          : b"ecac89cad93923c02321",
            "encode"       :  "EJDM8drfXA6uyA",
            "check_encode" :  "2W1Yd5Zu6WGyKVtHGMrH"
        },
        {
            "raw"          : b"10c8511e",
            "encode"       :  "Rt5zm",
            "check_encode" :  "3op3iuGMmhs"
        },
        {
            "raw"          : b"00000000000000000000",
            "encode"       :  "1111111111",
            "check_encode" :  "111111111146Momb"
        },
        {
            "raw"          : b"000111d38e5fc9071ffcd20b4a763cc9ae4f252bb4e48fd66a835e252ada93ff480d6dd43dc62a641155a5",
            "encode"       :  "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz",
            "check_encode" :  "17mxz9b2TuLnDf6XyQrHjAc3UvMoEg7YzRsJkBd4VwNpFh8a1StKmCe5WtAW27Y"
        },
        {
            "raw"          : b"000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff",
            "encode"       :  "1cWB5HCBdLjAuqGGReWE3R3CguuwSjw6RHn39s2yuDRTS5NsBgNiFpWgAnEx6VQi8csexkgYw3mdYrMHr8x9i7aEwP8kZ7vccXWqKDvGv3u1GxFKPuAkn8JCPPGDMf3vMMnbzm6Nh9zh1gcNsMvH3ZNLmP5fSG6DGbbi2tuwMWPthr4boWwCxf7ewSgNQeacyozhKDDQQ1qL5fQFUW52QKUZDZ5fw3KXNQJMcNTcaB723LchjeKun7MuGW5qyCBZYzA1KjofN1gYBV3NqyhQJ3Ns746GNuf9N2pQPmHz4xpnSrrfCvy6TVVz5d4PdrjeshsWQwpZsZGzvbdAdN8MKV5QsBDY",
            "check_encode" :  "151KWPPBRzdWPr1ASeu172gVgLf1YfUp6VJyk6K9t4cLqYtFHcMa2iX8S3NJEprUcW7W5LvaPRpz7UG7puBj5STE3nKhCGt5eckYq7mMn5nT7oTTic2BAX6zDdqrmGCnkszQkzkz8e5QLGDjf7KeQgtEDm4UER6DMSdBjFQVa6cHrrJn9myVyyhUrsVnfUk2WmNFZvkWv3Tnvzo2cJ1xW62XDfUgYz1pd97eUGGPuXvDFfLsBVd1dfdUhPwxW7pMPgdWHTmg5uqKGFF6vE4xXpAqZTbTxRZjCDdTn68c2wrcxApm8hq3JX65Hix7VtcD13FF8b7BzBtwjXq1ze6NMjKgUcqpGV5XA5"
        }
    ]

# Some base58 encoded strings with invalid checksum
TEST_VECTOR_CHK_ERR = \
    [
        "237LSrY9NUUar",
        "GwDDDeduj1jpykc27a",
        "2W1Yd5Zu6WGyKVtHGMrJ",
    ]

# Some base58 encoded strings with invalid encoding
TEST_VECTOR_ENC_ERR = \
    [
        "237LSrYONUUar",
        "GwDDDeduj1jpykc27I",
        "2WlYd5Zu6WGyKVtHGMrJ",
    ]


#
# Tests
#
class Base58Tests(unittest.TestCase):
    # Test decoder
    def test_decoder(self):
        for test in TEST_VECTOR:
            # Test decoder
            self.assertEqual(test["raw"], binascii.hexlify(Base58Decoder.Decode(test["encode"])))
            self.assertEqual(test["raw"], binascii.hexlify(Base58Decoder.CheckDecode(test["check_encode"])))

    # Test encoder
    def test_encoder(self):
        for test in TEST_VECTOR:
            # Test encoder
            self.assertEqual(test["encode"]      , Base58Encoder.Encode(binascii.unhexlify(test["raw"])))
            self.assertEqual(test["check_encode"], Base58Encoder.CheckEncode(binascii.unhexlify(test["raw"])))

    # Test invalid checksum
    def test_invalid_checksum(self):
        for test in TEST_VECTOR_CHK_ERR:
            self.assertRaises(RuntimeError, Base58Decoder.CheckDecode, test)

    # Test invalid encoding
    def test_invalid_encoding(self):
        for test in TEST_VECTOR_ENC_ERR:
            self.assertRaises(ValueError, Base58Decoder.Decode, test)


# Run test if executed
if __name__ == "__main__":
    unittest.main()
