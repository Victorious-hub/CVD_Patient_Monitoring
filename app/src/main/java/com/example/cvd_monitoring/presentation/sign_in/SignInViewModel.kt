package com.example.cvd_monitoring.presentation.sign_in

import android.util.Log
import androidx.compose.runtime.State
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cvd_monitoring.common.TextFieldState
import com.example.cvd_monitoring.domain.model.users.Auth
import com.example.cvd_monitoring.domain.model.users.CreateUserRequest
import com.example.cvd_monitoring.domain.model.users.User
import com.example.cvd_monitoring.domain.use_case.authenticate.UserAuthenticationUseCase
import com.example.cvd_monitoring.domain.use_case.sign_sup.CreatePatientUseCase
import com.example.cvd_monitoring.network.PatientApiService
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject


@HiltViewModel
class SignInViewModel @Inject constructor(
    private val userAuthenticationUseCase: UserAuthenticationUseCase
) : ViewModel(){
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

    fun authenticateUser() {
        val email = emailState.value.text
        val password = passwordState.value.text

        viewModelScope.launch {
            try {
                val patientUser = userAuthenticationUseCase(email, password)
                Log.d("SignInViewModel", "Sign in successful: $patientUser")
            } catch (e: Exception) {
                errorMessage = e.message.toString()
                Log.e("SignUpViewModel", "Sign up error: ${e.message}", e)
            }
        }
    }

}