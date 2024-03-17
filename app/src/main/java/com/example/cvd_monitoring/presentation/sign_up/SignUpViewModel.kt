package com.example.cvd_monitoring.presentation.sign_up

import android.util.Log
import androidx.compose.runtime.State
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cvd_monitoring.common.TextFieldState
import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
import com.example.cvd_monitoring.domain.model.users.User
import com.example.cvd_monitoring.domain.use_case.sign_sup.CreatePatientUseCase
import com.example.cvd_monitoring.network.PatientApiService
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class SignUpViewModel @Inject constructor(
    private val createPatientUseCase: CreatePatientUseCase
) : ViewModel(){
    private val _firstNameState = mutableStateOf(TextFieldState())
    val firstNameState: State<TextFieldState> = _firstNameState

    fun setFirstNameValue(value: String) {
        _firstNameState.value = firstNameState.value.copy(text = value)
    }

    private val _lastNameState = mutableStateOf(TextFieldState())
    val lastNameState: State<TextFieldState> = _lastNameState

    fun setLastNameValue(value: String) {
        _lastNameState.value = lastNameState.value.copy(text = value)
    }

    private val _emailState = mutableStateOf(TextFieldState())
    val emailState: State<TextFieldState> = _emailState

    fun setEmailValue(value: String) {
        _emailState.value = emailState.value.copy(text = value)
    }

    private val _passwordState = mutableStateOf(TextFieldState())
    val passwordState: State<TextFieldState> = _passwordState

    fun setPasswordValue(value: String) {
        _passwordState.value = passwordState.value.copy(text = value)
    }

    var errorMessage: String by mutableStateOf("")

    fun createPatient() {
        val firstName = firstNameState.value.text
        val lastName = lastNameState.value.text
        val email = emailState.value.text
        val password = passwordState.value.text

        viewModelScope.launch {
            try {
                val createdUser = createPatientUseCase(firstName, lastName, email, password)
                Log.d("SignUpViewModel", "Sign up successful: $createdUser")
            } catch (e: Exception) {
                errorMessage = e.message.toString()
                Log.e("SignUpViewModel", "Sign up error: $errorMessage", e)
            }
        }
    }
}
