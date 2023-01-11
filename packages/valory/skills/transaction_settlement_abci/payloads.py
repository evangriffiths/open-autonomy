# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2023 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the transaction payloads for common apps."""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional, Union

from packages.valory.skills.abstract_round_abci.base import (
    BaseTxPayload as BaseTxPayload,
)


class TransactionType(Enum):
    """Enumeration of transaction types."""

    VALIDATE = "validate_transaction"
    SIGNATURE = "signature_transaction"
    FINALIZATION = "finalization_transaction"
    RESET = "reset_transaction"
    RANDOMNESS = "randomness_transaction"
    SELECT_KEEPER = "select_keeper_transaction"
    CHECK = "check"
    SYNCHRONIZE = "synchronize"

    def __str__(self) -> str:
        """Get the string value of the transaction type."""
        return self.value


@dataclass(frozen=True)
class RandomnessPayload(BaseTxPayload):
    """Represent a transaction payload of type 'randomness'."""

    round_id: int
    randomness: str
    transaction_type = TransactionType.RANDOMNESS


@dataclass(frozen=True)
class SelectKeeperPayload(BaseTxPayload):
    """Represent a transaction payload of type 'select_keeper'."""

    keepers: str
    transaction_type = TransactionType.SELECT_KEEPER


@dataclass(frozen=True)
class ValidatePayload(BaseTxPayload):
    """Represent a transaction payload of type 'validate'."""

    vote: Optional[bool] = None
    transaction_type = TransactionType.VALIDATE


@dataclass(frozen=True)
class CheckTransactionHistoryPayload(BaseTxPayload):
    """Represent a transaction payload of type 'check'."""

    verified_res: str
    transaction_type = TransactionType.CHECK


@dataclass(frozen=True)
class SynchronizeLateMessagesPayload(BaseTxPayload):
    """Represent a transaction payload of type 'synchronize'."""

    tx_hashes: str
    transaction_type = TransactionType.SYNCHRONIZE


@dataclass(frozen=True)
class SignaturePayload(BaseTxPayload):
    """Represent a transaction payload of type 'signature'."""

    signature: str
    transaction_type = TransactionType.SIGNATURE


@dataclass(frozen=True)
class FinalizationTxPayload(BaseTxPayload):
    """Represent a transaction payload of type 'finalization'."""

    tx_data: Optional[Dict[str, Union[str, int, bool]]] = None
    transaction_type = TransactionType.FINALIZATION


@dataclass(frozen=True)
class ResetPayload(BaseTxPayload):
    """Represent a transaction payload of type 'reset'."""

    period_count: int
    transaction_type = TransactionType.RESET
