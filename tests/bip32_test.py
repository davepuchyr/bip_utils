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
from bip_utils import Bip32


# Tests from BIP32 page
TEST_VECTOR = \
    [
        {
            "seed" : b"000102030405060708090a0b0c0d0e0f",
            "master" :
                {
                    "ex_pub"  : "xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8",
                    "ex_priv" : "xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi",
                },
            "chains" :
                [
                        # m/0'
                        {
                            "path"    : "m/0'",
                            "index"   : Bip32.HardenIndex(0),
                            "ex_pub"  : "xpub68Gmy5EdvgibQVfPdqkBBCHxA5htiqg55crXYuXoQRKfDBFA1WEjWgP6LHhwBZeNK1VTsfTFUHCdrfp1bgwQ9xv5ski8PX9rL2dZXvgGDnw",
                            "ex_priv" : "xprv9uHRZZhk6KAJC1avXpDAp4MDc3sQKNxDiPvvkX8Br5ngLNv1TxvUxt4cV1rGL5hj6KCesnDYUhd7oWgT11eZG7XnxHrnYeSvkzY7d2bhkJ7",
                        },
                        # m/0'/1
                        {
                            "path"    : "m/0'/1",
                            "index"   : 1,
                            "ex_pub"  : "xpub6ASuArnXKPbfEwhqN6e3mwBcDTgzisQN1wXN9BJcM47sSikHjJf3UFHKkNAWbWMiGj7Wf5uMash7SyYq527Hqck2AxYysAA7xmALppuCkwQ",
                            "ex_priv" : "xprv9wTYmMFdV23N2TdNG573QoEsfRrWKQgWeibmLntzniatZvR9BmLnvSxqu53Kw1UmYPxLgboyZQaXwTCg8MSY3H2EU4pWcQDnRnrVA1xe8fs",
                        },
                        # m/0'/1/2'
                        {
                            "path"    : "m/0'/1/2'",
                            "index"   : Bip32.HardenIndex(2),
                            "ex_pub"  : "xpub6D4BDPcP2GT577Vvch3R8wDkScZWzQzMMUm3PWbmWvVJrZwQY4VUNgqFJPMM3No2dFDFGTsxxpG5uJh7n7epu4trkrX7x7DogT5Uv6fcLW5",
                            "ex_priv" : "xprv9z4pot5VBttmtdRTWfWQmoH1taj2axGVzFqSb8C9xaxKymcFzXBDptWmT7FwuEzG3ryjH4ktypQSAewRiNMjANTtpgP4mLTj34bhnZX7UiM",
                        },
                        # m/0'/1/2'/2
                        {
                            "path"    : "m/0'/1/2'/2",
                            "index"   : 2,
                            "ex_pub"  : "xpub6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6ZLRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV",
                            "ex_priv" : "xprvA2JDeKCSNNZky6uBCviVfJSKyQ1mDYahRjijr5idH2WwLsEd4Hsb2Tyh8RfQMuPh7f7RtyzTtdrbdqqsunu5Mm3wDvUAKRHSC34sJ7in334",
                        },
                        # m/0'/1/2'/2/1000000000
                        {
                            "path"    : "m/0'/1/2'/2/1000000000",
                            "index"   : 1000000000,
                            "ex_pub"  : "xpub6H1LXWLaKsWFhvm6RVpEL9P4KfRZSW7abD2ttkWP3SSQvnyA8FSVqNTEcYFgJS2UaFcxupHiYkro49S8yGasTvXEYBVPamhGW6cFJodrTHy",
                            "ex_priv" : "xprvA41z7zogVVwxVSgdKUHDy1SKmdb533PjDz7J6N6mV6uS3ze1ai8FHa8kmHScGpWmj4WggLyQjgPie1rFSruoUihUZREPSL39UNdE3BBDu76",
                        },
                ],
        },
        {
            "seed" : b"fffcf9f6f3f0edeae7e4e1dedbd8d5d2cfccc9c6c3c0bdbab7b4b1aeaba8a5a29f9c999693908d8a8784817e7b7875726f6c696663605d5a5754514e4b484542",
            "master" :
                {
                    "ex_pub"  : "xpub661MyMwAqRbcFW31YEwpkMuc5THy2PSt5bDMsktWQcFF8syAmRUapSCGu8ED9W6oDMSgv6Zz8idoc4a6mr8BDzTJY47LJhkJ8UB7WEGuduB",
                    "ex_priv" : "xprv9s21ZrQH143K31xYSDQpPDxsXRTUcvj2iNHm5NUtrGiGG5e2DtALGdso3pGz6ssrdK4PFmM8NSpSBHNqPqm55Qn3LqFtT2emdEXVYsCzC2U",
                },
            "chains" :
                [
                        # m/0
                        {
                            "path"    : "m/0",
                            "index"   : 0,
                            "ex_pub"  : "xpub69H7F5d8KSRgmmdJg2KhpAK8SR3DjMwAdkxj3ZuxV27CprR9LgpeyGmXUbC6wb7ERfvrnKZjXoUmmDznezpbZb7ap6r1D3tgFxHmwMkQTPH",
                            "ex_priv" : "xprv9vHkqa6EV4sPZHYqZznhT2NPtPCjKuDKGY38FBWLvgaDx45zo9WQRUT3dKYnjwih2yJD9mkrocEZXo1ex8G81dwSM1fwqWpWkeS3v86pgKt",
                        },
                        # m/0/2147483647'
                        {
                            "path"    : "m/0/2147483647'",
                            "index"   : Bip32.HardenIndex(2147483647),
                            "ex_pub"  : "xpub6ASAVgeehLbnwdqV6UKMHVzgqAG8Gr6riv3Fxxpj8ksbH9ebxaEyBLZ85ySDhKiLDBrQSARLq1uNRts8RuJiHjaDMBU4Zn9h8LZNnBC5y4a",
                            "ex_priv" : "xprv9wSp6B7kry3Vj9m1zSnLvN3xH8RdsPP1Mh7fAaR7aRLcQMKTR2vidYEeEg2mUCTAwCd6vnxVrcjfy2kRgVsFawNzmjuHc2YmYRmagcEPdU9",
                        },
                        # m/0/2147483647'/1
                        {
                            "path"    : "m/0/2147483647'/1",
                            "index"   : 1,
                            "ex_pub"  : "xpub6DF8uhdarytz3FWdA8TvFSvvAh8dP3283MY7p2V4SeE2wyWmG5mg5EwVvmdMVCQcoNJxGoWaU9DCWh89LojfZ537wTfunKau47EL2dhHKon",
                            "ex_priv" : "xprv9zFnWC6h2cLgpmSA46vutJzBcfJ8yaJGg8cX1e5StJh45BBciYTRXSd25UEPVuesF9yog62tGAQtHjXajPPdbRCHuWS6T8XA2ECKADdw4Ef",
                        },
                        # m/0/2147483647'/1/2147483646'
                        {
                            "path"    : "m/0/2147483647'/1/2147483646'",
                            "index"   : Bip32.HardenIndex(2147483646),
                            "ex_pub"  : "xpub6ERApfZwUNrhLCkDtcHTcxd75RbzS1ed54G1LkBUHQVHQKqhMkhgbmJbZRkrgZw4koxb5JaHWkY4ALHY2grBGRjaDMzQLcgJvLJuZZvRcEL",
                            "ex_priv" : "xprvA1RpRA33e1JQ7ifknakTFpgNXPmW2YvmhqLQYMmrj4xJXXWYpDPS3xz7iAxn8L39njGVyuoseXzU6rcxFLJ8HFsTjSyQbLYnMpCqE2VbFWc",
                        },
                        # m/0/2147483647'/1/2147483646'/2
                        {
                            "path"    : "m/0/2147483647'/1/2147483646'/2",
                            "index"   : 2,
                            "ex_pub"  : "xpub6FnCn6nSzZAw5Tw7cgR9bi15UV96gLZhjDstkXXxvCLsUXBGXPdSnLFbdpq8p9HmGsApME5hQTZ3emM2rnY5agb9rXpVGyy3bdW6EEgAtqt",
                            "ex_priv" : "xprvA2nrNbFZABcdryreWet9Ea4LvTJcGsqrMzxHx98MMrotbir7yrKCEXw7nadnHM8Dq38EGfSh6dqA9QWTyefMLEcBYJUuekgW4BYPJcr9E7j",
                        },
                ],
        },
        {
            "seed" : b"4b381541583be4423346c643850da4b320e46a87ae3d2a4e6da11eba819cd4acba45d239319ac14f863b8d5ab5a0d0c64d2e8a1e7d1457df2e5a3c51c73235be",
            "master" :
                {
                    "ex_pub"  : "xpub661MyMwAqRbcEZVB4dScxMAdx6d4nFc9nvyvH3v4gJL378CSRZiYmhRoP7mBy6gSPSCYk6SzXPTf3ND1cZAceL7SfJ1Z3GC8vBgp2epUt13",
                    "ex_priv" : "xprv9s21ZrQH143K25QhxbucbDDuQ4naNntJRi4KUfWT7xo4EKsHt2QJDu7KXp1A3u7Bi1j8ph3EGsZ9Xvz9dGuVrtHHs7pXeTzjuxBrCmmhgC6",
                },
            "chains" :
                [
                        # m/0'
                        {
                            "path"    : "m/0'",
                            "index"   : Bip32.HardenIndex(0),
                            "ex_pub"  : "xpub68NZiKmJWnxxS6aaHmn81bvJeTESw724CRDs6HbuccFQN9Ku14VQrADWgqbhhTHBaohPX4CjNLf9fq9MYo6oDaPPLPxSb7gwQN3ih19Zm4Y",
                            "ex_priv" : "xprv9uPDJpEQgRQfDcW7BkF7eTya6RPxXeJCqCJGHuCJ4GiRVLzkTXBAJMu2qaMWPrS7AANYqdq6vcBcBUdJCVVFceUvJFjaPdGZ2y9WACViL4L",
                        },
                ],
        },
    ]


#
# Tests
#
class Bip32Tests(unittest.TestCase):
    # Run all tests in test vector using ChildKey for derivation
    def test_vector_child_key(self):
        for test in TEST_VECTOR:
            # Create from seed
            bip32_ctx = Bip32.FromSeed(binascii.unhexlify(test["seed"]))

            # Test master key
            self.assertEqual(test["master"]["ex_pub"] , bip32_ctx.ExtendedPublicKey())
            self.assertEqual(test["master"]["ex_priv"], bip32_ctx.ExtendedPrivateKey())

            # Test chains
            for chain in test["chains"]:
                # Update context
                bip32_ctx = bip32_ctx.ChildKey(chain["index"])
                # Test keys
                self.assertEqual(chain["ex_pub"] , bip32_ctx.ExtendedPublicKey())
                self.assertEqual(chain["ex_priv"], bip32_ctx.ExtendedPrivateKey())

    # Run all tests in test vector using DerivePath for derivation
    def test_vector_derive_path(self):
        for test in TEST_VECTOR:
            # Create from seed
            bip32_ctx = Bip32.FromSeed(binascii.unhexlify(test["seed"]))

            # Test master key
            self.assertEqual(test["master"]["ex_pub"] , bip32_ctx.ExtendedPublicKey())
            self.assertEqual(test["master"]["ex_priv"], bip32_ctx.ExtendedPrivateKey())

            # Test chains
            for chain in test["chains"]:
                # Update context
                bip32_from_path = bip32_ctx.DerivePath(chain["path"][2:])
                # Test keys
                self.assertEqual(chain["ex_pub"] , bip32_from_path.ExtendedPublicKey())
                self.assertEqual(chain["ex_priv"], bip32_from_path.ExtendedPrivateKey())

    # Run all tests in test vector using FromSeedAndPath
    def test_vector_from_path(self):
        for test in TEST_VECTOR:
            # Create from seed
            bip32_ctx = Bip32.FromSeedAndPath(binascii.unhexlify(test["seed"]), "m")

            # Test master key
            self.assertEqual(test["master"]["ex_pub"] , bip32_ctx.ExtendedPublicKey())
            self.assertEqual(test["master"]["ex_priv"], bip32_ctx.ExtendedPrivateKey())

            # Test chains
            for chain in test["chains"]:
                # Try to build from path and test again
                bip32_from_path = Bip32.FromSeedAndPath(binascii.unhexlify(test["seed"]), chain["path"])
                self.assertEqual(chain["ex_pub"] , bip32_from_path.ExtendedPublicKey())
                self.assertEqual(chain["ex_priv"], bip32_from_path.ExtendedPrivateKey())


# Run test if executed
if __name__ == "__main__":
    unittest.main()
