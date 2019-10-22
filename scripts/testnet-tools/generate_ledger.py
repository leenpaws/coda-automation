#!/usr/bin/env python3

import pubkey_to_discord
import offline_keys

content = """
open Functor.Without_private
module Public_key = Signature_lib.Public_key

include Make (struct
  let accounts =
    (* VRF Account *)
    [ { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNEJsZZgAKgcuuqtRs8cb3SDJAfTdwpbAdg6aNnV2WZXftd2USKNFc6VPU7KtFZD1JNnCzWq3ygaioNNxqw1d6DW4KyR8MhNthdLDQMYK2nwz8zeCWUm6EQpREnvQDw11khpbKoyBX9uJ"
      ; balance= 1000
      ; delegate= None }
      (* O(1) Proposer Account Pair 1 *)
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDky3tTyWUdf1iccjh8zqga1yATQQ6r5Q7qdbtaVHntT9ncGsgRfHiqHsJsNiXUSzSTDyq2FRK3eJC3XNvf4KBRy7KELNKxQCsj7ycgV3XxPydzALPMmjFJ4v7mASXLMYYaAK6Dkqk5f"
      ; balance= 10000000
      ; delegate=
          Some
            (Public_key.Compressed.of_base58_check_exn
               "tdNDs39Vk2rLLy9o43yNVBFrouEY9p49SHQjSyV4vvX7wpi52x1k3Eykg8soVmwLFDqJBfF3vvKWZuz2xjaQT9opUA5P2miTpJwP1RGu9vm2mM1gFcZxNd1fHBY8Jggezr7We9qCShZwCY")
      }
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDs39Vk2rLLy9o43yNVBFrouEY9p49SHQjSyV4vvX7wpi52x1k3Eykg8soVmwLFDqJBfF3vvKWZuz2xjaQT9opUA5P2miTpJwP1RGu9vm2mM1gFcZxNd1fHBY8Jggezr7We9qCShZwCY"
      ; balance= 1000
      ; delegate= None }
      (* O(1) Proposer Account Pair 2 *)
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNEHktzZep3DHVJJxvvtVD91ZoSvoLgtxAL7fCMGZC1Qtdso28DuuossMggsBgJkbhptzH2cFuQ7U5n6FaZraxA4sB6ex3xDHF8gEgdNYisfAg5n7eHUz4AAikM866fc7hCk9n7wrwMQj"
      ; balance= 10000000
      ; delegate=
          Some
            (Public_key.Compressed.of_base58_check_exn
               "tdNE2pXYz8vGxvqVjcA59pw2qfnkotFdKeVnnmKy1Loh9HXGnoHnLn24Mvsci8GQM1EdMHSs5TCWxVjGAU1ysfKSWZ9kcuJV6Ez2bExyXdqy2kRg5rJCHFX6Ek6oRNve2WdmDnvtswjtRZ")
      }
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNE2pXYz8vGxvqVjcA59pw2qfnkotFdKeVnnmKy1Loh9HXGnoHnLn24Mvsci8GQM1EdMHSs5TCWxVjGAU1ysfKSWZ9kcuJV6Ez2bExyXdqy2kRg5rJCHFX6Ek6oRNve2WdmDnvtswjtRZ"
      ; balance= 1000
      ; delegate= None }
      (* O(1) Proposer Account Pair 3 *)
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDeLpBdTppcxxoxJzgAQFpmzzMkNjWA9bhcCLDDzkd6sR4y8rhpKfXrfMgxMviNK5ncc7UVx4effUxpNNqpwr7SDtopAin4dSb4wkDXRAax7dgnvTe5p7sp7DSmKKYPe6Vp9hEq1En9i"
      ; balance= 10000000
      ; delegate=
          Some
            (Public_key.Compressed.of_base58_check_exn
               "tdNDypcUkVoNSsbdhT9ytXwVxxU2ECEhaLsgq2ceiBzRxQonBtxsofVs9BAjb43BrWf5rUs5ewRyogkiaWddSkGNhXQHCk8FtJ4HDUfPARHMYstvEP2h9CWuE5t1MdUD1Q9tXDPJRMy2qq")
      }
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDypcUkVoNSsbdhT9ytXwVxxU2ECEhaLsgq2ceiBzRxQonBtxsofVs9BAjb43BrWf5rUs5ewRyogkiaWddSkGNhXQHCk8FtJ4HDUfPARHMYstvEP2h9CWuE5t1MdUD1Q9tXDPJRMy2qq"
      ; balance= 1000
      ; delegate= None }
      (* O(1) Proposer Account Pair 4 *)
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDmQzS1Vy6TeTND8cg1h9Swr5CJNTa666Yxj9QHKAQ557PP2HebGX944HQ71usJmLYCXRPXy1X9RRs4eDxwNFf5koHMsBYjK3MSsBMFD1g7VuTXm1tVNze33VrUbDdiTuWecdXBnMS9R"
      ; balance= 10000000
      ; delegate=
          Some
            (Public_key.Compressed.of_base58_check_exn
               "tdNDsh6jrSfinUQdrUXxD4KSNbTy9HYL5eX83RXaYSEB6CQMEuyTrdb8vkUuKdpqLeNmpw7qppNKcNoZzKAJDREaXAFT3iz5gvJbxVoXQQ8A8En9k24QBD9pjbM3WEVY4Az5arf93qnyGW")
      }
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDsh6jrSfinUQdrUXxD4KSNbTy9HYL5eX83RXaYSEB6CQMEuyTrdb8vkUuKdpqLeNmpw7qppNKcNoZzKAJDREaXAFT3iz5gvJbxVoXQQ8A8En9k24QBD9pjbM3WEVY4Az5arf93qnyGW"
      ; balance= 1000
      ; delegate= None }
      (* O(1) Proposer Account Pair 5 *)
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDx1Ct9JvFYHbwtpggvsMgpZGn2BoG3ny41r5CNXhDiaYcdgjQLYTrrmH5BEAqyvTtvbzEeQFCGKcNUp9HWPyy1P1DdXTHwnPsNLyvf19LvaBwzyBZxQqPQNp6vSF9XRULmJPLGkvg62"
      ; balance= 10000000
      ; delegate=
          Some
            (Public_key.Compressed.of_base58_check_exn
               "tdNDjjAwyjgvNgU1x8uWs1n44H8vK7UGrRLvXzkcv8iC3Jw9A1B1UDUZndgBZh6zTb23pNatt7ujfTbCVjiihTZRMJcErZSkz93qE5Ue5VpAJsvaQvpHQGj3XexP2fK6i6xMfQArSvcXWV")
      }
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDjjAwyjgvNgU1x8uWs1n44H8vK7UGrRLvXzkcv8iC3Jw9A1B1UDUZndgBZh6zTb23pNatt7ujfTbCVjiihTZRMJcErZSkz93qE5Ue5VpAJsvaQvpHQGj3XexP2fK6i6xMfQArSvcXWV"
      ; balance= 1000
      ; delegate= None }
      (* Faucet Key *)
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNE67M9Snd4KF2Y3xgCQ8Res8LQxckx5xpraAAfa9uv1P6GUy8a6QkXbLnN8PknuKDknEerRCYGujScean4D88v5sJcTqiuqnr2666Csc8QhpUW6MeXq7MgEha7S6ttxB3bY9MMVrDNBB"
      ; balance= 5000000
      ; delegate=
          Some
            (Public_key.Compressed.of_base58_check_exn
               "tdNDs39Vk2rLLy9o43yNVBFrouEY9p49SHQjSyV4vvX7wpi52x1k3Eykg8soVmwLFDqJBfF3vvKWZuz2xjaQT9opUA5P2miTpJwP1RGu9vm2mM1gFcZxNd1fHBY8Jggezr7We9qCShZwCY")
      }
      (* Echo Key *)
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "tdNDk6tKpzhVXUqozR5y2r77pppsEak7icvdYNsv2dbKx6r69AGUUbQsfrHHquZipQCmMj4VRhVF3u4F5NDgdbuxxWANULyVjUYPbe85fv7bpjKRgSpGR3zo2566s5GNNKQyLRUm12wt5o"
      ; balance= 5000000
      ; delegate=
          Some
            (Public_key.Compressed.of_base58_check_exn
               "tdNDs39Vk2rLLy9o43yNVBFrouEY9p49SHQjSyV4vvX7wpi52x1k3Eykg8soVmwLFDqJBfF3vvKWZuz2xjaQT9opUA5P2miTpJwP1RGu9vm2mM1gFcZxNd1fHBY8Jggezr7We9qCShZwCY")
      }
      (* User Stake Keys *)
"""

total_user_accounts = len(pubkey_to_discord.STAKING_CHALLENGE)

coda_per_user = int(80000000 / total_user_accounts)

id = 1
for (user_key, discord_id) in pubkey_to_discord.STAKING_CHALLENGE.items():
    offline_key = offline_keys.OFFLINE_PUBLIC_KEYS[id]
    content += """
      (* Offline/Online User Keys: %s   %s of %s *)
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "%s"
      ; balance= %s
      ; delegate=
          Some
            (Public_key.Compressed.of_base58_check_exn
               "%s")
      }
    ; { pk=
          Public_key.Compressed.of_base58_check_exn
            "%s"
      ; balance= 1000
      ; delegate= None }""" % (discord_id, id, total_user_accounts,
                               offline_key, coda_per_user, user_key, user_key)
    id += 1

content += """]
end)"""

print(content)
