package com.example.cvd_monitoring.presentation

import com.example.cvd_monitoring.domain.model.users.Patient

data class CurrentUserState(
    val patient: Patient? = null,
    val error: String = ""
)
