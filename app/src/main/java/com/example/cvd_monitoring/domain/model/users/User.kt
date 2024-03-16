package com.example.cvd_monitoring.domain.model.users

import android.provider.ContactsContract.CommonDataKinds.Email

data class User(
    val first_name: String,
    val last_name: String,
    val email: String,
    val password: String
)

data class CreateUserRequest(
    val user: User
)